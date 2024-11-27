from enum import Enum

# Enumerator para a seleção do ambiente de execução do Usuário
class StatusEncomenda(Enum):
	PRODUZIDA = "[Produzida]"
	CARREGADA = "[Carregada]"
	TRANSPORTE = "[Transporte]"
	DESPACHE = "[Despache]"
	ENTREGUE = "[Entregue]"

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
        self.status = StatusEncomenda.PRODUZIDA             #Status da encomenda

    def anotar_rastro(self):

        self.status = StatusEncomenda.ENTREGUE
        trecho_producao = f'{self.horario_producao}ms'
        trecho_carregamento = f'{self.horario_carregamento}ms'
        trecho_despacho = f'{self.horario_despacho}ms'

        if self.horario_producao > 999:
            trecho_producao = str(int(self.horario_producao/1000)) + "s"
        if self.horario_carregamento > 999:
            trecho_carregamento = str(int(self.horario_carregamento/1000)) + "s"
        if self.horario_despacho > 999:
            trecho_despacho = str(int(self.horario_despacho/1000)) + "s"
        with open('rastro.txt', 'a') as arquivo:
            arquivo.write(f'\nEncomenda {self.id}:\nProduto: {self.nome}\nOrigem: Ponto de Distribuicao {self.origem}\nDestino: Ponto de Distribuicao {self.destino}\nHorario de Producao: {trecho_producao}\nHorario de Carregamento: {trecho_carregamento} - Caminhao {self.nome_caminhao}\nHorario de Despacho: {trecho_despacho} - Caminhao {self.nome_caminhao}\n')

    #Método de impressão da Classe
    def __str__(self):
        return f'- {self.nome}'

    #Método de leitura de valores
    def __repr__(self):
        return f'Encomenda(origem={self.origem}, destino={self.destino}, id={self.id})'