import time, threading
from typing import List
from queue import Queue
from encomenda import Encomenda
from caminhao import Caminhao

class CentroDistribuicao:
    def __init__(self, id: str):
        self.encomendas = []
        self.fila_caminhoes = Queue()
        self.id = id
        self.lock = threading.Lock()

    def __str__(self):
        return f'Ponto de Distribuição com {len(self.encomendas)} encomendas e {self.fila_caminhoes.qsize()} caminhões na fila'

    def __repr__(self):
        return f'PontoDeDistribuicao(encomendas={self.encomendas}, fila_caminhoes={list(self.fila_caminhoes.queue)})'
    
    def adicionar_encomenda(self, encomenda: Encomenda):
        if encomenda not in self.encomendas:
            self.encomendas.append(encomenda)
            print(f"Encomenda \"{encomenda}\" foi registrada no centro {self.id}")
            return True
        return False
    
    def remover_encomenda(self, encomenda: Encomenda):
        if encomenda in self.encomendas:
            return self.encomendas.remove(encomenda)
        return None
    
    def adicionar_caminhao_na_fila(self, caminhao: Caminhao):
        self.fila_caminhoes.put(caminhao)

    def remover_caminhao_da_fila(self):
        if(not self.fila_caminhoes.empty()):
            return self.fila_caminhoes.get()
        return None
