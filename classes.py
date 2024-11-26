class Caminhao:

    #Construtor
    def __init__(self, capacidade: int):
        self.capacidade = capacidade
        self.encomendas = []

    #Método de impressão da capacidade da classe
    def __str__(self):
        return f'Caminhao com capacidade para {self.capacidade} encomendas'

    #Método de leitura de valores
    def __repr__(self):
        return f'Caminhao(capacidade={self.capacidade})'

    #Método de carregamento de encomendas
    def carregar(self, encomenda):
        if isinstance(encomenda, Encomenda) and len(self.encomendas) < self.capacidade:
            self.encomendas.append(encomenda)
            return True
        return False

    #Método de descarregamento de encomendas
    def descarregar(self, origem: int):

        for encomenda in self.encomendas:
            if encomenda.destino == origem:
                self.encomendas.remove(encomenda)

    #Método de listagem de encomendas
    def espacos_disponiveis(self):
        return self.capacidade - len(self.encomendas)

    #Método para adicionar encomendas
    def adicionar_encomenda(self, encomenda):
        if isinstance(encomenda, Encomenda) and len(self.encomendas) < self.capacidade:
            self.encomendas.append(encomenda)
            return True
        return False

    #Método para remover encomendas
    def remover_encomenda(self, encomenda):
        if encomenda in self.encomendas:
            self.encomendas.remove(encomenda)

    #Método para listar encomendas
    def listar_encomendas(self):
        return self.encomendas

class Encomenda:

    #Construtor
    def __init__(self, destino: str, nome: str, origem: str):
        if destino == origem:
            raise ValueError("Origem e destino não podem ser iguais")
        self.destino = destino
        self.nome = nome
        self.remetente = origem

    #Método de impressão da Classe
    def __str__(self):
        return f'Encomenda {self.nome} de origem \"{self.origem}\" para destino \"{self.origem}\"'

    #Método de leitura de valores
    def __repr__(self):
        return f'Encomenda(destino={self.destino}, nome={self.nome}, origem={self.origem})'

    #Método para atualizar o destino da encomenda
    def atualizar_destino(self, novo_destino: str):
        self.destino = novo_destino

    #Método para atualizar o nome da encomenda
    def atualizar_nome(self, novo_nome: str):
        self.nome = novo_nome

    #Método para atualizar a origem da encomenda
    def atualizar_remetente(self, nova_origem: str):
        self.origem = nova_origem

class PontoDeRedistribuicao:

    #Construtor
    def __init__(self):
        self.encomendas = []

    #Método de adicionar encomendas
    def adicionar_encomenda(self, encomenda):
        if isinstance(encomenda, Encomenda):
            self.encomendas.append(encomenda)

    #Método de remover encomendas
    def remover_encomenda(self, encomenda):
        if encomenda in self.encomendas:
            self.encomendas.remove(encomenda)

    #Método de listar encomendas
    def listar_encomendas(self):
        return self.encomendas

    #Método de impressão da quantidade de encomendas
    def __str__(self):
        return f'Ponto de Redistribuição com {len(self.encomendas)} encomendas'

    #Método de leitura de valores
    def __repr__(self):
        return f'PontoDeRedistribuicao(encomendas={self.encomendas})'

