import time
from typing import List
from encomenda import Encomenda

class Caminhao:

    def __init__(self, capacidade: int, localizacao: int, id):
        self.id = id
        self.capacidade = capacidade
        self.localizacao = localizacao
        self.carga: List[Encomenda] = []
        self.esperando = False

    def __str__(self):
        return f'{self.id} com capacidade para {self.capacidade} encomendas'

    def __repr__(self):
        return f'Caminhao(capacidade={self.capacidade}, localizacao={self.localizacao}, id={self.id})'

    def espacos_disponiveis(self):
        return self.capacidade - len(self.carga)

    def adicionar_encomenda(self, encomenda: Encomenda):
        if self.espacos_disponiveis() > 0:
            encomenda.id_caminhao = self.id
            encomenda.horario_carregamento = time.time()
            self.carga.append(encomenda)
            print(f"Encomenda \"{encomenda}\" foi adicionada ao caminhao {self.id}")
            return encomenda
        return None

    def remover_encomenda(self, encomenda: Encomenda):
        if encomenda in self.carga:
            print(f"Encomenda \"{encomenda}\" foi removida do caminhao {self.id}")
            return self.carga.remove(encomenda)
        return None