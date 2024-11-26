import threading
import random
import time
from classes import Caminhao, Encomenda, PontoDeDistribuicao
from enum import Enum, auto
from typing import List


encomendas_em_execucao = 0
#encomendas_em_execucao_lock = threading.Lock()

class Ambiente(Enum):
    PROMPT = auto()
    APLICACAO = auto()

class Entrada:
    def __init__(self, pontos_distribuicao, caminhoes, encomendas, capacidade_carga):
        self.S = pontos_distribuicao
        self.C = caminhoes
        self.P = encomendas
        self.A = capacidade_carga

    def __str__(self):
        return str(f'\nEntrada:\n(S) Pontos de Distribuição: {self.S}\n(C) Caminhões: {self.C}\n(P) Encomendas: {self.P}\n(A) Capacidade de Carga: {self.A}\n')

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


def ponto_distribuicao(id, pontos, tempo_inicial):
    print(f"Ponto de Distribuicao {id}")
    ponto:PontoDeDistribuicao = pontos[id]
    global encomendas_em_execucao
    while encomendas_em_execucao > 0:
        caminhao = ponto.processar_caminhao(id, tempo_inicial)
        if caminhao:
            print(f"Caminhao {caminhao.id} processado no Ponto de Distribuicao {id}")

def caminhao(entrada:Entrada, pontos:List[PontoDeDistribuicao]):
    caminhao = Caminhao(entrada.A, random.randint(0, entrada.S - 1), threading.current_thread().name)
    global encomendas_em_execucao
    while encomendas_em_execucao > 0:
        pontos[caminhao.localizacao].adicionar_caminhao(caminhao)
        print(f"{caminhao.id} adicionado à fila do Ponto de Distribuicao {caminhao.localizacao}")

        while(caminhao.esperando):
            time.sleep(10E-5)

        time.sleep(random.randint(1,1000) * 10E-5)

        caminhao.localizacao=caminhao.localizacao+1
        if (caminhao.localizacao == entrada.S):
            caminhao.localizacao = 0

def encomenda(args,tempo_inicial):
    id = args['id']
    entrada = args['entrada']
    pontos:List[PontoDeDistribuicao] = args['pontos']

    origem = random.randint(0, entrada.S - 1)
    destino = random.randint(0, entrada.S - 1)
    while destino == origem:
        destino = random.randint(0, entrada.S - 1)
    
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

    entrada:Entrada = Entrada(0, 0, 0, 0)
    entrada.leitura_valores(Ambiente.PROMPT)
    print(entrada)

    semaforo = threading.Semaphore()
    pontos = [PontoDeDistribuicao() for _ in range(entrada.S)]
    threads_pontos_distribuicao = []
    threads_caminhoes = []
    threads_encomendas = []
    tempo_inicial = time.time()

    for i in range(entrada.S):
        thread = threading.Thread(target=ponto_distribuicao, args=(i, pontos, tempo_inicial), name=f"PontoDeDistribuicao {i}")
        threads_pontos_distribuicao.append(thread)
        thread.start()

    for i in range(entrada.C):
        thread = threading.Thread(target=caminhao, args=(entrada, pontos), name=f"Caminhao {i}")
        threads_caminhoes.append(thread)
        thread.start()

    for i in range(entrada.P):
        args = {'id': i, 'entrada': entrada, 'pontos': pontos}
        thread = threading.Thread(target=encomenda, args=(args,tempo_inicial), name=f"Encomenda {i}")
        threads_encomendas.append(thread)
        thread.start()


    # "Free" dos Threads
    for thread in threads_encomendas + threads_caminhoes + threads_pontos_distribuicao:
        print(f"{thread.name} liberado")
        thread.join()