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

    # ...existing code...
