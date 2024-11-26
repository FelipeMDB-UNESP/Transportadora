class Encomenda:

    #Construtor
    def __init__(self, destino: str, nome: str, origem: str):
        if destino == origem:
            raise ValueError("Origem e destino não podem ser iguais")
        self.destino = destino
        self.nome = nome
        self.origem = origem
        self.id_caminhao = None
        self.horario_chegada = None
        self.horario_carregamento = None
        self.horario_descarregamento = None

    #Método de impressão da Classe
    def __str__(self):
        return f'Encomenda {self.nome} de origem \"{self.origem}\" para destino \"{self.origem}\"'

    #Método de leitura de valores
    def __repr__(self):
        return f'Encomenda(destino={self.destino}, nome={self.nome}, origem={self.origem})'

    # Métodos para manipular os atributos
    def set_destino(self, destino):
        self.destino = destino

    def get_destino(self):
        return self.destino

    def set_nome(self, nome):
        self.nome = nome

    def get_nome(self):
        return self.nome

    def set_remetente(self, remetente):
        self.remetente = remetente

    def get_remetente(self):
        return self.remetente

    def set_horario_chegada(self, horario):
        self.horario_chegada = horario

    def get_horario_chegada(self):
        return self.horario_chegada

    def set_horario_carregamento(self, horario):
        self.horario_carregamento = horario

    def get_horario_carregamento(self):
        return self.horario_carregamento

    def set_id_caminhao(self, id_caminhao):
        self.id_caminhao = id_caminhao

    def get_id_caminhao(self):
        return self.id_caminhao

    def set_horario_descarregamento(self, horario):
        self.horario_descarregamento = horario

    def get_horario_descarregamento(self):
        return self.horario_descarregamento

class Caminhao:

    #Construtor
    def __init__(self, capacidade: int, id: int):
        self.capacidade = capacidade
        self.id = id
        self.encomendas = []

    #Método de impressão da capacidade da classe
    def __str__(self):
        return f'Caminhao {self.id} com capacidade para {self.capacidade} encomendas'

    #Método de leitura de valores
    def __repr__(self):
        return f'Caminhao(capacidade={self.capacidade}, id={self.id})'

    #Método de listagem de encomendas
    def espacos_disponiveis(self):
        return self.capacidade - len(self.encomendas)

    #Método de carregamento de encomendas
    def carregar(self, encomenda: Encomenda):
        return self.adicionar_encomenda(encomenda)

    #Método de descarregamento de encomendas
    def descarregar(self, origem: int):

        for encomenda in self.encomendas:
            if encomenda.destino == origem:
                self.remover_encomenda(encomenda)

    #Método para adicionar encomendas
    def adicionar_encomenda(self, encomenda: Encomenda):
        if self.espacos_disponiveis() > 0:
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

