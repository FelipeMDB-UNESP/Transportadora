from queue import Queue
from typing import List
import threading
import time
import random

class Encomenda:

    #Construtor
    def __init__(self, origem: str, destino: str, nome: str):
        if destino == origem:
            raise ValueError("Origem e destino não podem ser iguais")
        self.destino = destino
        self.nome = nome
        self.origem = origem
        self.id_caminhao = None
        self.horario_chegada = None
        self.horario_carregamento = None
        self.horario_descarregamento = None
        self.condition = threading.Condition()

    #Método de impressão da Classe
    def __str__(self):
        return f'Encomenda {self.nome} de origem \"{self.origem}\" para destino \"{self.origem}\" pelo {self.id_caminhao} inicializada no tempo {self.horario_chegada}, carregada em {self.horario_carregamento} e descarregada em {self.horario_descarregamento}'

    #Método de leitura de valores
    def __repr__(self):
        return f'Encomenda(destino={self.destino}, nome={self.nome}, origem={self.origem})'
    
    def esperar_descarregamento(self):
        with self.condition:
            self.condition.wait()

    def notificar_descarregamento(self):
        with self.condition:
            self.condition.notify()

class Caminhao:

    #Construtor
    def __init__(self, capacidade: int, localizacao: int, id):
        self.capacidade = capacidade
        self.localizacao = localizacao
        self.id = id
        self.encomendas = []
        self.esperando = False

    #Método de impressão da capacidade da classe
    def __str__(self):
        return f'{self.id} com capacidade para {self.capacidade} encomendas'

    #Método de leitura de valores
    def __repr__(self):
        return f'Caminhao(capacidade={self.capacidade}, localizacao={self.localizacao}, id={self.id})'

    #Método de listagem de encomendas
    def espacos_disponiveis(self):
        return self.capacidade - len(self.encomendas)

    #Método de carregamento de encomendas
    def carregar(self, encomendas: List[Encomenda], tempo_inicial):
        for encomenda in encomendas:
            if self.espacos_disponiveis() > 0:
                time.sleep(random.randint(1,1000) * 10E-5)
                encomenda.id_caminhao = self.id
                self.encomendas.append(encomenda)
                encomenda.horario_carregamento = time.time() - tempo_inicial
            else:
                break
    

    #Método de descarregamento de encomendas
    def descarregar(self, tempo_inicial):
        for encomenda in self.encomendas:
            if encomenda.destino == self.localizacao:
                time.sleep(random.randint(1,1000) * 10E-5)
                encomenda.horario_descarregamento = time.time() - tempo_inicial
                self.remover_encomenda(encomenda)
                encomenda.notificar_descarregamento()
            else:
                print(f"{encomenda.nome} não é para o local {self.localizacao}")

    #Método para adicionar encomendas
    def adicionar_encomenda(self, encomenda: Encomenda):
        if self.espacos_disponiveis() > 0:
            encomenda.id_caminhao = self.id
            self.encomendas.append(encomenda)
            print(f"Encomenda \"{encomenda}\" foi adicionada ao caminhao {self.id}")
            return True
        return False

    #Método para remover encomendas
    def remover_encomenda(self, encomenda):
        if encomenda in self.encomendas:
            print(f"Encomenda \"{encomenda}\" foi removida do caminhao {self.id}")
            self.encomendas.remove(encomenda)

    #Método para listar encomendas
    def listar_encomendas(self):
        return self.encomendas

class PontoDeDistribuicao:
    def __init__(self):
        self.encomendas = []
        self.fila_caminhoes = Queue()
        self.mutex = threading.Lock()

    def __str__(self):
        return f'Ponto de Redistribuição com {len(self.encomendas)} encomendas e {self.fila_caminhoes.qsize()} caminhões na fila'

    def __repr__(self):
        return f'PontoDeRedistribuicao(encomendas={self.encomendas}, fila_caminhoes={list(self.fila_caminhoes.queue)})'

    def adicionar_encomenda(self, encomenda: Encomenda):
        if encomenda not in self.encomendas:
            self.encomendas.append(encomenda)
            return True
        return False

    def remover_encomenda(self, encomenda: Encomenda):
        if encomenda in self.encomendas:
            self.encomendas.remove(encomenda)

    def listar_encomendas(self):
        return self.encomendas
    
    def adicionar_caminhao(self, caminhao: Caminhao):
        with self.mutex:
            if not caminhao.esperando:
                self.fila_caminhoes.put(caminhao)
                caminhao.esperando = True

    def remover_caminhao(self):
        with self.mutex:
            if not self.fila_caminhoes.empty():
                caminhao = self.fila_caminhoes.get()
                return caminhao
        return None

    def processar_caminhao(self, id: int, tempo_inicial):
        with self.mutex:
            if not self.fila_caminhoes.empty():
                caminhao:Caminhao = self.remover_caminhao()
                print(f"Caminhao {caminhao.id} está sendo processado no ponto de redistribuição")
                caminhao.descarregar(tempo_inicial)
                #threading.Event().wait(1)
                caminhao.carregar(self.encomendas,tempo_inicial)
                caminhao.esperando = False
                print(f"Caminhao {caminhao.id} saiu do ponto de redistribuição")
                return caminhao
        return None

