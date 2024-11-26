import threading
import sys
from classes import Caminhao, Encomenda, PontoDeDistribuicao
from app import Entradas

# Funções para threads
def ponto_distribuicao(id):
    print(f"Ponto de Distribuicao {id}")

def caminhao(id):
    print(f"Caminhao {id}")

def encomenda(id):
    print(f"Pacote {id}")

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
    threads_pontos = []
    threads_caminhoes = []
    threads_encomendas = []

    # Criar threads para pontos de redistribuição
    for i in range(S):
        thread = threading.Thread(target=ponto_distribuicao, args=(i,))
        thread.setName(f"PontoDeDistribuicao {i}")
        threads_pontos.append(thread)
        thread.start()

    # Criar threads para caminhões
    for i in range(C):
        thread = threading.Thread(target=caminhao, args=(i,))
        thread.setName(f"Caminhao {i}")
        threads_caminhoes.append(thread)
        thread.start()

    # Criar threads para encomendas
    for i in range(P):
        thread = threading.Thread(target=encomenda, args=(i,))
        thread.setName(f"Encomenda {i}")
        threads_encomendas.append(thread)
        thread.start()

    # "Free" dos Threads
    for thread in threads_pontos + threads_caminhoes + threads_encomendas:
        print(f"{thread.name} liberado")
        thread.join()