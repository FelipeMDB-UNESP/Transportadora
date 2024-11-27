from classes.entradas import Entradas,Ambiente
from service import manipular_threads
from classes.caminhao import Caminhao
from classes.encomenda import Encomenda

import time
tempo_inicial = time.time()

ambiente = Ambiente.TESTE

# main:
entradas = Entradas(3, 4, 6, 5)  # valores default para testes & inicialização do objeto
entradas.leitura_valores(ambiente) #pede ao usuário preencher cada campo de entrada
print(entradas)

manipular_threads(entradas)







#testes
caminhao = Caminhao(entradas.A, 1, "Caminhao 1")
encomendas = ["arroz", "feijao", "cenoura", "bife role", "alface", "tomate", "suco de laranja", "chocolate", "cafe", "pao"]

for i in range(entradas.P):
    encomenda = Encomenda(entradas.S, encomendas[i], f"Encomenda {i}",tempo_inicial)
    time.sleep(5 * 10E-6)
    encomenda.horario_carregamento = time.time() - tempo_inicial
    time.sleep(15 * 10E-6)
    encomenda.horario_despacho = time.time() - tempo_inicial
    encomenda.anotar_rastro()
    caminhao.adicionar_encomenda(encomenda)

caminhao.listar_encomendas()