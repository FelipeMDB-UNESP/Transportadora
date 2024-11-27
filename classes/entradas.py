import sys
from enum import Enum, auto

# Enumerator para a seleção do ambiente de execução do Usuário
class Ambiente(Enum):
    TESTE = auto()
    PROMPT = auto()
    APLICACAO = auto()
    DEFAULT = auto()

# Classe de Entradas, contendo os valores iniciais do problema
class Entradas:
    def __init__(self, pontos_distribuicao, caminhoes, encomendas, capacidade_carga):
        self.S = pontos_distribuicao
        self.C = caminhoes
        self.P = encomendas
        self.A = capacidade_carga

    def __str__(self):
        return str(f'\nEntradas:\n(S) Pontos de Distribuição: {self.S}\n(C) Caminhões: {self.C}\n(P) Encomendas: {self.P}\n(A) Capacidade de Carga: {self.A}\n')

    def leitura_argumentos(self):
        if len(sys.argv) == 5:
            self.S = int(sys.argv[1])
            self.C = int(sys.argv[2])
            self.P = int(sys.argv[3])
            self.A = int(sys.argv[4])

    def leitura_valores(self, ambiente):

        if ambiente is Ambiente.TESTE:
            self.leitura_argumentos()

        if ambiente is Ambiente.PROMPT:
            while True:
                self.S = int(input("\nDigite a quantidade de Pontos de Distribuição: "))
                self.C = int(input("Digite a quantidade de Caminhões: "))
                self.P = int(input("Digite a quantidade de Encomendas a serem entregues: "))
                self.A = int(input("Digite a capacidade de carga dos Caminhões: "))

                if self.P > self.A and self.A > self.C:
                    break
                print("\nCondições iniciais não suportadas, refazendo as requisições...\n")
        
        if ambiente is Ambiente.APLICACAO:
            pass                            #possivel adicao ao fazer interacao por tela
        
        if ambiente is Ambiente.DEFAULT:
            pass
