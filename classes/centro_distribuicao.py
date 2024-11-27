import time
import threading
from queue import Queue
from encomenda import Encomenda
from caminhao import Caminhao

class CentroDistribuicao:
    def __init__(self, id: str):
        self.encomendas = []
        self.fila_caminhoes = Queue()
        self.id = id
        self.lock = threading.Lock()

    
    def adicionar_encomenda(self, encomenda: Encomenda, tempo_inicial):
        if encomenda not in self.encomendas:
            self.encomendas.append(encomenda)
            encomenda.horario_producao = int((time.time() - tempo_inicial) * 1000)
            print(f"Encomenda {encomenda.id} foi registrada no centro {self.id}")
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

    #Método de listar encomendas
    def listar_encomendas(self):
        print("\nEncomendas do " + self.id + ":")
        for encomenda in self.encomendas:
            print("-" + encomenda)
        print("\n")
        return self.encomendas
    
    #Método de impressão geral na tela
    def __str__(self):
        return f'Ponto de Distribuição com {len(self.encomendas)} encomendas e {self.fila_caminhoes.qsize()} caminhões na fila.'

    #Método de leitura de valores aos programadores
    def __repr__(self):
        return f'PontoDeDistribuicao(encomendas={self.encomendas}, fila_caminhoes={list(self.fila_caminhoes.queue)})'