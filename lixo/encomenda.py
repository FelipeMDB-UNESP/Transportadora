import time
import random

class Encomenda:

    #Construtor
    def __init__(self, pontos_distribuicao: int, nome: str, id: str, tempo_inicial):
        self.id = id
        self.nome = nome
        self.origem = random.randint(0, pontos_distribuicao-1)
        self.destino = random.randint(0, pontos_distribuicao-1)

        while self.destino == self.origem:
            self.destino = random.randint(0, pontos_distribuicao-1)
        
        self.id_caminhao = "Caminhao Ausente"
        self.horario_producao = time.time() - tempo_inicial
        self.horario_carregamento = None
        self.horario_despacho = None

    def anotar_rastro(self):
        with open('rastro.txt', 'a') as arquivo:
            arquivo.write(f'\n{self.id}:\nProduto: {self.nome}\nOrigem: Ponto de Distribuicao {self.origem}\nDestino: Ponto de Distribuicao {self.destino}\nHorario de Producao: {self.horario_producao}\nHorario de Carregamento: {self.horario_carregamento} - {self.id_caminhao}\nHorario de Despacho: {self.horario_despacho} - {self.id_caminhao}\n')

    #Método de impressão da Classe
    def __str__(self):
        return f'- {self.nome}'

    #Método de leitura de valores
    def __repr__(self):
        return f'Encomenda(origem={self.origem}, destino={self.destino}, nome={self.nome})'