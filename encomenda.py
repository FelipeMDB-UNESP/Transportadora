import threading

class Encomenda:

    def __init__(self, origem: str, destino: str, id: int):
        self.destino = destino                              #destino da encomenda
        self.id = id                                    #nome da encomenda
        self.origem = origem                                #origem da encomenda
        self.id_caminhao = None                             #id do caminhao que transporta a encomenda
        self.horario_chegada_na_origem = None               #horario de chegada à origem
        self.horario_carregamento = None                    #horario de carregamento da encomenda no caminhao        
        self.horario_descarregamento = None                 #horario de descarregamento da encomenda no destino

    def __str__(self):
        return f'Encomenda {self.id} de origem \"{self.origem}\" para destino \"{self.destino}\"'

    def __repr__(self):
        return f'Encomenda(destino={self.destino}, nome={self.id}, origem={self.origem})'