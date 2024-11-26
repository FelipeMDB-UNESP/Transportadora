import time
import random
import threading
from enum import Enum, auto
from classes import Caminhao, Encomenda, PontoDeDistribuicao

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

                if self.P > self.A and self.A > self.C:
                    break
                print("\nCondições iniciais não suportadas, refazendo as requisições...\n")

# '''TODO:
# -Insertion Sort
# -Class ponto_distribuicao
# -Class pacote
# -Class caminhao
# -Threads:
#   -ponto_distribuicao
#   -pacote
#   -caminhao'''

def ponto_distribuicao(a):
    print("\nPonto de Distribuicao:", a)

dado = 1

def caminhao(a):
    print("\nCaminhao:", a)

def ponto_distribuicao():
    print("\nPonto de Distribuicao:")

def caminhao():
    global dado
    semaforo.acquire(blocking=True)  # decrementa
    mutex.acquire()  # incrementa
    print("\nEntrega:" + str(dado))
    dado = dado + 1
    mutex.release()  # decrementa
    semaforo.release()  # incrementa

def pacote():
    print("\nPacote:")

mutex = threading.Lock()
semaforo = threading.Semaphore()
threads_caminhoes = []

# Inicialização dos Threads
for i in range(100):
    thread = threading.Thread(target=caminhao)
    thread.setName("Caminhao " + str(i))
    threads_caminhoes.append(thread)
    thread.start()

# "Free" dos Threads
for thread in threads_caminhoes:
    print("\n" + thread.name + " liberado")
    thread.join()

def pacote(a):
    print("\nPacote:", a)

def teste(a):
    pass

# main:
entradas = Entradas(3, 4, 6, 5)  # valores default para testes & inicialização do objeto
# ambiente = Ambiente.PROMPT   #vide enumerator
# entradas.leitura_valores(ambiente) #pede ao usuário preencher cada campo de entrada
print(entradas)