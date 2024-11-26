class Caminhao:
    def __init__(self, capacidade: int):
        self.capacidade = capacidade
        self.encomendas = []

    def __str__(self):
        return f'Caminhao com capacidade para {self.capacidade} encomendas'

    def __repr__(self):
        return f'Caminhao(capacidade={self.capacidade})'

    def carregar(self, encomenda):
        if isinstance(encomenda, Encomenda) and len(self.encomendas) < self.capacidade:
            self.encomendas.append(encomenda)
            return True
        return False

    def descarregar(self, quantidade: int):
        pass

    def espacos_disponiveis(self):
        return self.capacidade - len(self.encomendas)

    def adicionar_encomenda(self, encomenda):
        if isinstance(encomenda, Encomenda) and len(self.encomendas) < self.capacidade:
            self.encomendas.append(encomenda)
            return True
        return False

    def remover_encomenda(self, encomenda):
        if encomenda in self.encomendas:
            self.encomendas.remove(encomenda)

    def listar_encomendas(self):
        return self.encomendas

class Encomenda:
    def __init__(self, destino: str, nome: str, origem: str):
        if destino == origem:
            raise ValueError("Origem e destino não podem ser iguais")
        self.destino = destino
        self.nome = nome
        self.remetente = origem

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

    # ...existing code...
