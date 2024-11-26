import threading
import sys
from classes import Caminhao, Encomenda, PontoDeDistribuicao
from app import Entradas
import random

# Funções para threads
def ponto_distribuicao(id):
    while True:
        with mutex:
            if not pontos_distribuicao[id].fila_caminhoes.empty():
                caminhao_id = pontos_distribuicao[id].fila_caminhoes.get()
                print(f"Ponto de Distribuicao {id} atendendo Caminhao {caminhao_id}")
        # Simulate some work
        threading.Event().wait(1)

def caminhao():
    caminhao = Caminhao(entradas.A, random.randint(0, entradas.S - 1), threading.current_thread().name)
    pontos_distribuicao[caminhao.localizacao].fila_caminhoes.put(caminhao.id)
    print(caminhao)

def encomenda(id):
    print(f"Pacote {id}")

# A --> espaços de carga
# C --> caminhões
# P --> encomendas
# S --> pontos de distribuição
# main:
if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Uso: python service.py <S> <C> <P> <A>")
        sys.exit(1)

    S = int(sys.argv[1])
    C = int(sys.argv[2])
    P = int(sys.argv[3])
    A = int(sys.argv[4])

    entradas = Entradas(S, C, P, A)
    print(entradas)

    mutex = threading.Lock()
    semaforo = threading.Semaphore()
    pontos = [[] for _ in range(S)]
    threads_pontos_distribuicao = []
    threads_caminhoes = []
    threads_encomendas = []
    
    pontos_distribuicao = [None for _ in range(entradas.S)]

    for i in range(entradas.S):
        pontos_distribuicao[i] = PontoDeDistribuicao()

    # Criar threads para pontos de distribuição
    for i in range(S):
        thread = threading.Thread(target=ponto_distribuicao, name=f"PontoDeDistribuicao {i}")
        threads_pontos_distribuicao.append(thread)
        thread.start()

    # Criar threads para caminhões
    for i in range(C):
        thread = threading.Thread(target=caminhao, name=f"Caminhao {i}")
        threads_caminhoes.append(thread)
        thread.start()

    # Criar threads para encomendas
    for i in range(P):
        thread = threading.Thread(target=encomenda, name=f"Encomenda {i}")
        threads_encomendas.append(thread)
        thread.start()

    # "Free" dos Threads
    for thread in threads_pontos_distribuicao + threads_caminhoes + threads_encomendas:
        print(f"{thread.name} liberado")
        thread.join()