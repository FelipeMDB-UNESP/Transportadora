import time
import threading
from classes.entradas import Entradas
from classes.caminhao import Caminhao
from classes.encomenda import Encomenda
from classes.ponto_distribuicao import PontoDistribuicao

# Funções para threads
def ponto_distribuicao():
    print(threading.current_thread().name)
    time.sleep(2 * 10E-6)

def caminhao():
    print(threading.current_thread().name)
    time.sleep(2 * 10E-6)

def encomenda():
    print(threading.current_thread().name)
    time.sleep(2 * 10E-6)


# Criar threads para encomendas
def inicializar_encomendas(threads, entradas: Entradas):
    for i in range(entradas.P):
        thread = threading.Thread(target=encomenda, args=())
        thread.setName(f"Encomenda {i}")
        threads.append(thread)
        thread.start()

# Criar threads para caminhões
def inicializar_caminhoes(threads, entradas: Entradas):
    for i in range(entradas.C):
        thread = threading.Thread(target=caminhao, args=())
        thread.setName(f"Caminhao {i}")
        threads.append(thread)
        thread.start()

# Criar threads para pontos de distribuição
def inicializar_pontos_distribuicao(threads, entradas: Entradas):
    for i in range(entradas.S):
        thread = threading.Thread(target=ponto_distribuicao, args=())
        thread.setName(f"PontoDistribuicao {i}")
        threads.append(thread)
        thread.start()

# Liberacao dos threads ja terminados
def liberar_threads(threads):
    for thread in threads:
        print(f"{thread.name} liberado")
        thread.join()
    tempo_final = time.time() - tempo_inicial
    print("\nO programa durou " + str(tempo_final) + " segundos para sua execucao completa.")

# Manipulacao geral das threads
def manipular_threads(entradas: Entradas):

    global tempo_inicial
    tempo_inicial = time.time()
    with open('rastro.txt', 'w') as arquivo:
        arquivo.write("Arquivo de Rastro:\n")

    threads_pontos_distribuicao = []
    inicializar_pontos_distribuicao(threads_pontos_distribuicao, entradas)

    threads_encomendas = []
    inicializar_encomendas(threads_encomendas, entradas)

    threads_caminhoes = []
    inicializar_caminhoes(threads_caminhoes, entradas)

    liberar_threads(threads_encomendas + threads_pontos_distribuicao + threads_caminhoes)





# Exemplo de Mutex e Semaforo:

# mutex = threading.Lock()
# semaforo = threading.Semaphore()

# def caminhao():
#     global dado
#     semaforo.acquire(blocking=True)  # decrementa
#     mutex.acquire()  # incrementa
#     print("\nEntrega:" + str(dado))
#     dado = dado + 1
#     mutex.release()  # decrementa
#     semaforo.release()  # incrementa
