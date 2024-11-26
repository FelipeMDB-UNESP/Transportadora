class Caminhao:
    def __init__(self, espacos_de_carga: int):
        self.espacos_de_carga = espacos_de_carga

    def __str__(self):
        return f'Caminhao com {self.espacos_de_carga} espaços de carga'

    def __repr__(self):
        return f'Caminhao(espacos_de_carga={self.espacos_de_carga})'

    def carregar(self, quantidade: int):
        if quantidade <= self.espacos_de_carga:
            self.espacos_de_carga -= quantidade
            return True
        return False

    def descarregar(self, quantidade: int):
        self.espacos_de_carga += quantidade

    def verificar_espacos(self):
        return self.espacos_de_carga


class Encomenda:
    def __init__(self, destino: str, nome: str, remetente: str):
        self.destino = destino
        self.nome = nome
        self.remetente = remetente

    def __str__(self):
        return f'Encomenda {self.nome} para {self.destino} de {self.remetente}'

    def __repr__(self):
        return f'Encomenda(destino={self.destino}, nome={self.nome}, remetente={self.remetente})'

    def atualizar_destino(self, novo_destino: str):
        self.destino = novo_destino

    def atualizar_nome(self, novo_nome: str):
        self.nome = novo_nome

    def atualizar_remetente(self, novo_remetente: str):
        self.remetente = novo_remetente

