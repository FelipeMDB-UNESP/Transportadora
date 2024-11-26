import threading
import sys
from classes import Caminhao, Encomenda, PontoDeDistribuicao
from enum import Enum, auto
import random
import time


encomendas_em_execucao = 0
encomendas_em_execucao_lock = threading.Lock()

# Enumerator para a seleção do ambiente de execução do Usuário
class Ambiente(Enum):
    PROMPT = auto()
    APLICACAO = auto()

# Classe de Entradas, contendo os valores iniciais do problema
class Entradas:
    def __init__(self, pontos_distribuicao, caminhoes, encomendas, capacidade_carga):
        self.S = pontos_distribuicao
        self.C = caminhoes
        self.P = encomendas
        self.A = capacidade_carga

    def __str__(self):
        return str(f'\nEntradas:\n(S) Pontos de Distribuição: {self.S}\n(C) Caminhões: {self.C}\n(P) Encomendas: {self.P}\n(A) Capacidade de Carga: {self.A}\n')

    def leitura_valores(self, ambiente):
        if ambiente is Ambiente.PROMPT:
            while True:
                self.S = int(input("\nDigite a quantidade de Pontos de Distribuição: "))
                self.C = int(input("Digite a quantidade de Caminhões: "))
                self.P = int(input("Digite a quantidade de Encomendas a serem entregues: "))
                self.A = int(input("Digite a capacidade de carga dos Caminhões: "))
                global encomendas_em_execucao
                encomendas_em_execucao = self.P

                if self.P > self.A and self.A > self.C:
                    break
                print("\nCondições iniciais não suportadas, refazendo as requisições...\n")


# Funções para threads
def ponto_distribuicao(id, pontos, tempo_inicial):
    print(f"Ponto de Distribuicao {id}")
    ponto = pontos[id]
    global encomendas_em_execucao
    while encomendas_em_execucao > 0:
        caminhao = ponto.processar_caminhao(id, tempo_inicial)
        if caminhao:
            print(f"Caminhao {caminhao.id} processado no Ponto de Distribuicao {id}")

def caminhao(entradas, pontos):
    caminhao = Caminhao(entradas.A, random.randint(0, entradas.S - 1), threading.current_thread().name)
    global encomendas_em_execucao
    while encomendas_em_execucao > 0:
        pontos[caminhao.localizacao].adicionar_caminhao(caminhao)
        print(f"{caminhao.id} adicionado à fila do Ponto de Distribuicao {caminhao.localizacao}")

        while(caminhao.esperando):
            time.sleep(10E-5)

        time.sleep(random.randint(1,1000) * 10E-5)

        caminhao.localizacao=caminhao.localizacao+1
        if (caminhao.localizacao == entradas.S):
            caminhao.localizacao = 0

def encomenda(args,tempo_inicial):
    id = args['id']
    entradas = args['entradas']
    pontos = args['pontos']

    origem = random.randint(0, entradas.S - 1)
    destino = random.randint(0, entradas.S - 1)
    while destino == origem:
        destino = random.randint(0, entradas.S - 1)
    
    encomenda = Encomenda(origem, destino, threading.current_thread().name)
    pontos[origem].adicionar_encomenda(encomenda)
    encomenda.horario_chegada = time.time() - tempo_inicial

    print(f"Encomenda {id} criado e adicionado ao Ponto de Distribuicao {origem}")
    
    encomenda.esperar_descarregamento()

    print(f"Encomenda {id} foi descarregado no destino {destino}")
    global encomendas_em_execucao 
    encomendas_em_execucao -= 1
    print(encomenda)
    print(f"Encomendas em execução: {encomendas_em_execucao}")




# A --> espaços de carga
# C --> caminhões
# P --> encomendas
# S --> pontos de distribuição
# main:
if __name__ == "__main__":
    # if len(sys.argv) != 5:
    #     print("Uso: python service.py <S> <C> <P> <A>")
    #     sys.exit(1)

    # S = int(sys.argv[1])
    # C = int(sys.argv[2])
    # P = int(sys.argv[3])
    # A = int(sys.argv[4])

    entradas = Entradas(0, 0, 0, 0)
    entradas.leitura_valores(Ambiente.PROMPT)
    print(entradas)

    semaforo = threading.Semaphore()
    pontos = [PontoDeDistribuicao() for _ in range(entradas.S)]
    threads_pontos_distribuicao = []
    threads_caminhoes = []
    threads_encomendas = []
    tempo_inicial = time.time()

    # Criar threads para pontos de distribuição
    for i in range(entradas.S):
        thread = threading.Thread(target=ponto_distribuicao, args=(i, pontos, tempo_inicial), name=f"PontoDeDistribuicao {i}")
        threads_pontos_distribuicao.append(thread)
        thread.start()

    # Criar threads para caminhões
    for i in range(entradas.C):
        thread = threading.Thread(target=caminhao, args=(entradas, pontos), name=f"Caminhao {i}")
        threads_caminhoes.append(thread)
        thread.start()

    # Criar threads para encomendas
    for i in range(entradas.P):
        args = {'id': i, 'entradas': entradas, 'pontos': pontos}
        thread = threading.Thread(target=encomenda, args=(args,tempo_inicial), name=f"Encomenda {i}")
        threads_encomendas.append(thread)
        thread.start()


    # # "Free" dos Threads
    for thread in threads_encomendas + threads_caminhoes + threads_pontos_distribuicao:
        print(f"{thread.name} liberado")
        thread.join()