import time
import random
from typing import List
from classes.encomenda import Encomenda

class Caminhao:

    def __init__(self, capacidade: int, localizacao: int, id):
        self.id = id
        self.capacidade = capacidade
        self.localizacao = localizacao
        self.carga: List[Encomenda] = []
        self.esperando = False

    #Método para consumir tempo entre pontos de distribuicao
    def estrada(self):
        time.sleep(random.uniform(1, 3))

    def espacos_disponiveis(self):
        return self.capacidade - len(self.carga)

    #Método para listar encomendas
    def listar_encomendas(self):
        print("\nEncomendas do " + self.id + ":")
        for carga in self.carga:
            print(str(carga))
        print("\n")
        return self.carga

    def adicionar_encomenda(self, encomenda: Encomenda, tempo_inicial):
        if self.espacos_disponiveis() > 0:
            encomenda.id_caminhao = self.id
            encomenda.nome_caminhao = self.id
            encomenda.horario_carregamento = int((time.time() - tempo_inicial) * 1000)
            self.carga.append(encomenda)
            return encomenda
        return None

    def remover_encomenda(self, encomenda: Encomenda):
        if encomenda in self.carga:
            return self.carga.remove(encomenda)
        return None
    
    #Método de impressão da capacidade da classe
    def __str__(self):
        return f'{self.id} com espacos para {self.espacos_disponiveis()} encomendas está no ponto {self.localizacao}.'

    #Método de leitura de valores
    def __repr__(self):
        return f'Caminhao(capacidade={self.capacidade}, localizacao={self.localizacao}, id={self.id})'