from enum import Enum, auto


class Ambiente(Enum):
    PROMPT = auto()
    APLICACAO = auto()

class Entrada:
    def __init__(self, pontos_distribuicao, caminhoes, encomendas, capacidade_carga):
        self.S = pontos_distribuicao
        self.C = caminhoes
        self.P = encomendas
        self.A = capacidade_carga

    def __str__(self):
        return str(f'\nEntrada:\n(S) Pontos de Distribuição: {self.S}\n(C) Caminhões: {self.C}\n(P) Encomendas: {self.P}\n(A) Capacidade de Carga: {self.A}\n')

    def leitura_valores(self, ambiente):
        if ambiente is Ambiente.PROMPT:
            while True:
                self.S = int(input("\nDigite a quantidade de Pontos de Distribuição: "))
                self.C = int(input("Digite a quantidade de Caminhões: "))
                self.P = int(input("Digite a quantidade de Encomendas a serem entregues: "))
                self.A = int(input("Digite a capacidade de carga dos Caminhões: "))
                global encomendas_em_execucao
                encomendas_em_execucao = self.P

                if self.P > self.A and self.A > self.C:
                    break
                print("\nCondições iniciais não suportadas, refazendo as requisições...\n")