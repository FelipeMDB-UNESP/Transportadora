class Encomenda:

    def __init__(self, origem: str, destino: str, nome: str, id: int):
        self.id = id                                        #id da encomenda
        self.nome = nome                                    #produto da encomenda
        self.origem = origem                                #origem da encomenda
        self.destino = destino                              #destino da encomenda
        self.id_caminhao = None                             #id do caminhao que transporta a encomenda
        self.nome_caminhao = "Ausente"                      #Nome do caminhao que levara a mercadoria
        self.horario_producao = None                        #horario de chegada à origem
        self.horario_carregamento = None                    #horario de carregamento da encomenda no caminhao        
        self.horario_despacho = None                        #horario de descarregamento da encomenda no destino

    def anotar_rastro(self):
        with open('rastro.txt', 'a') as arquivo:
            arquivo.write(f'\nEncomenda {self.id}:\nProduto: {self.nome}\nOrigem: Ponto de Distribuicao {self.origem}\nDestino: Ponto de Distribuicao {self.destino}\nHorario de Producao: {self.horario_producao}ms\nHorario de Carregamento: {self.horario_carregamento}ms - Caminhao {self.nome_caminhao}\nHorario de Despacho: {self.horario_despacho}ms - Caminhao {self.nome_caminhao}\n')

    #Método de impressão da Classe
    def __str__(self):
        return f'- {self.nome}'

    #Método de leitura de valores
    def __repr__(self):
        return f'Encomenda(origem={self.origem}, destino={self.destino}, id={self.id})'