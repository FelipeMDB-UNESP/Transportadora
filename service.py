from classes import Caminhao, Encomenda, PontoDeDistribuicao
from app import Entradas
import random
import threading

entradas = Entradas(3, 4, 6, 5)  # valores default para testes & inicialização do objeto

pontos = [None for i in range(entradas.S)]

random.seed()

for i in range(entradas.S):
    pontos[i] = PontoDeDistribuicao()

def thread_caminhao():

    caminhao = Caminhao(entradas.A, random.randint(1,entradas.S), threading.current_thread().name)