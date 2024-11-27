import time
import random
import threading
from classes.caminhao import Caminhao
from classes.encomenda import Encomenda, StatusEncomenda
from classes.entradas import Entradas, Ambiente
from classes.centro_distribuicao import CentroDistribuicao

def thread_encomenda(encomenda: Encomenda, centros: list[CentroDistribuicao], condition: threading.Condition, all_delivered: threading.Event):

    centro_origem: CentroDistribuicao = centros[encomenda.origem]
    centro_destino: CentroDistribuicao = centros[encomenda.destino]

    with centro_origem.lock:
        centro_origem.adicionar_encomenda(encomenda, tempo_inicial)
        print(f"Encomenda [{encomenda.id}] adicionada ao centro de origem [{centro_origem.id}]")
    
    with condition:
        print(f"Encomenda [{encomenda.id}] foi notificada para aguardar")
        while encomenda.id_caminhao is None:
            condition.wait()

    print(f"Encomenda [{encomenda.id}] está sendo transportada pelo caminhão [{encomenda.id_caminhao}]")
    encomenda.status = StatusEncomenda.TRANSPORTE
    Caminhao.estrada()  # Simular viagem

    while encomenda.id_caminhao is not None:

        for caminhao in caminhoes:

            if caminhao.id == encomenda.id_caminhao and caminhao.localizacao == centro_destino.id:
                encomenda.status = StatusEncomenda.DESPACHE
                time.sleep(random.randint(1,5))
                encomenda.horario_despacho = int((time.time() - tempo_inicial) * 1000)
                encomenda.anotar_rastro()
                caminhao.remover_encomenda(encomenda)
                encomenda.id_caminhao = None

                with condition:
                    condition.notify_all()
                print(f"Encomenda [{encomenda.id}] foi descarregada no centro de destino [{centro_destino.id}] pelo caminhão [{caminhao.id}]")
                break

def thread_caminhao(caminhao: Caminhao, centros: list[CentroDistribuicao], condition: threading.Condition, all_delivered: threading.Event):

    atual = caminhao.localizacao

    while True:

        print(f"Caminhão [{caminhao.id}] chegou ao centro [{centros[atual].id}]")
        with centros[atual].lock:

            caminhao.localizacao = centros[atual].id

            if not centros[atual].fila_caminhoes.empty():
                caminhao.esperando = True
                centros[atual].adicionar_caminhao_na_fila(caminhao)
                print(f"Caminhão [{caminhao.id}] esperando no centro [{centros[atual].id}]")
                while caminhao.esperando:
                    time.sleep(1)

            else:
                caminhao.esperando = False

                while caminhao.espacos_disponiveis() > 0 and centros[atual].encomendas:
                    time.sleep(random.randint(1,5))
                    encomenda = centros[atual].encomendas.pop(0)
                    encomenda.status = StatusEncomenda.CARREGADA
                    caminhao.adicionar_encomenda(encomenda,tempo_inicial)

                    with condition:
                        condition.notify_all()
                    print(f"Encomenda [{encomenda.id}] carregada no caminhão [{caminhao.id}] no centro [{centros[atual].id}]")
                Caminhao.estrada()  # Simular viagem
            
        if all(not centro.encomendas and centro.fila_caminhoes.empty() for centro in centros) and not caminhao.carga:
            print(f"Caminhão [{caminhao.id}] finalizou suas entregas")
            break

        if atual < len(centros)-1:
            atual = atual+1
        else:
            atual=0
        
    all_delivered.set()


if __name__ == "__main__":
    entrada = Entradas(5, 5, 100, 6)
    entrada.leitura_valores(Ambiente.PROMPT)
    print(entrada)

    global tempo_inicial
    tempo_inicial = time.time()
    with open('rastro.txt', 'w') as arquivo:
        arquivo.write("Arquivo de Rastro:\n")

    produtos = ["Arroz", "Feijao", "Cenoura", "Alface", "Tomate", "Cafe", "Trigo", "Soja", "Batata"]
    centros = [CentroDistribuicao(i) for i in range(entrada.S)]
    caminhoes = [Caminhao(entrada.A, random.choice(centros).id, i) for i in range(entrada.C)]
    encomendas:list[Encomenda] = []
    for i in range(entrada.P):
        origem = random.choice(centros).id
        destino = random.choice(centros).id
        while origem == destino:
            destino = random.choice(centros).id
        encomendas.append(Encomenda(origem, destino, random.choice(produtos), i))

    print(f"Total de encomendas: {len(encomendas)}")  # Debug print

    condition = threading.Condition()
    all_delivered = threading.Event()
    threads = []

    # Create threads for encomendas
    for encomenda in encomendas:
        t = threading.Thread(target=thread_encomenda, args=(encomenda, centros, condition, all_delivered))
        threads.append(t)
        t.start()

    # Ensure all encomenda threads are created
    if len(threads) != len(encomendas):
        raise RuntimeError(f"Expected {len(encomendas)} encomenda threads, but created {len(threads)}")

    # Create threads for caminhoes
    for caminhao in caminhoes:
        t = threading.Thread(target=thread_caminhao, args=(caminhao, centros, condition, all_delivered))
        threads.append(t)
        t.start()

    # Ensure all caminhao threads are created
    if len(threads) != len(encomendas) + len(caminhoes):
        raise RuntimeError(f"Expected {len(encomendas) + len(caminhoes)} total threads, but created {len(threads)}")

    all_delivered.wait()
    for t in threads:
        t.join()
        print(f"Thread {t.name} finalizada")