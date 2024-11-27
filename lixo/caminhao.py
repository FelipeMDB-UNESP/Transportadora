import time
import random
from classes.encomenda import Encomenda

class Caminhao:

    #Construtor
    def __init__(self, capacidade: int, localizacao: int, id):
        self.capacidade = capacidade
        self.localizacao = localizacao
        self.cargas = []
        self.id = id

    #Método para consumir tempo entre pontos de distribuicao
    def estrada():
        time.sleep(random.randint(1,1024) * 10E-6)

    #Método de listagem de encomendas
    def espacos_disponiveis(self):
        return self.capacidade - len(self.cargas)

    #Método para listar encomendas
    def listar_encomendas(self):
        print("\nEncomendas do " + self.id + ":")
        for carga in self.cargas:
            print(str(carga))
        print("\n")
        return self.cargas

    #Método de descarregamento de encomendas
    def descarregar(self, tempo_inicial):
        descarregou = False
        for carga in self.cargas:
            if carga.destino == self.localizacao:
                descarregou = self.remover_encomenda(carga)
                carga.horario_descarregamento = time.time() - tempo_inicial
        return descarregou
    
    #Método de carregamento de encomendas
    def carregar(self, encomendas, tempo_inicial):
        carregou = False
        while self.espacos_disponiveis() > 0:
            encomenda = encomendas.pop()
            encomenda.horario_carregamento = time.time() - tempo_inicial
            encomenda.id_caminhao = self.id
            carregou = self.adicionar_encomenda(encomenda)
        return carregou

    #Método para adicionar encomendas
    def adicionar_encomenda(self, encomenda: Encomenda):
        self.cargas.append(encomenda)
        return True

    #Método para remover encomendas
    def remover_encomenda(self, encomenda: Encomenda):
        self.cargas.remove(encomenda)
        return True

    #Método de impressão da capacidade da classe
    def __str__(self):
        return f'{self.id} com espacos para {self.espacos_disponiveis()} encomendas está no ponto {self.localizacao}.'

    #Método de leitura de valores
    def __repr__(self):
        return f'Caminhao(capacidade={self.capacidade}, localizacao={self.localizacao}, id={self.id})'