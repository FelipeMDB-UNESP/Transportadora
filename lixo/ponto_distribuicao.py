from classes.encomenda import Encomenda

class PontoDistribuicao:

    #Construtor
    def __init__(self):
        self.encomendas = []

    #Método de adicionar encomendas
    def adicionar_encomenda(self, encomenda: Encomenda):
        self.encomendas.append(encomenda)
        return True

    #Método de remover encomendas
    def remover_encomenda(self, encomenda: Encomenda):
        self.encomendas.remove(encomenda)
        return True

    #Método de listar encomendas
    def listar_encomendas(self):
        print("\nEncomendas do " + self.id + ":")
        for encomenda in self.encomendas:
            print("-" + encomenda)
        print("\n")
        return self.encomendas

    #Método de impressão da quantidade de encomendas
    def __str__(self):
        return f'Ponto de Distribuição com {len(self.encomendas)} encomendas.'

    #Método de leitura de valores
    def __repr__(self):
        return f'PontoDistribuicao(encomendas={self.encomendas})'