# Sistema de Logística com Threads

Este projeto simula um sistema de logística utilizando threads para representar encomendas e caminhões que transitam entre centros de distribuição. O programa é escrito em Python e utiliza concorrência para simular o fluxo de transporte de encomendas entre diferentes centros.

## Funcionalidades

- **Simulação de Centros de Distribuição**: Gerenciam encomendas e caminhões em trânsito.
- **Transporte de Encomendas**: Caminhões recolhem encomendas em um centro de origem e as entregam em um centro de destino.
- **Uso de Threads**: Cada encomenda e caminhão é gerenciado em uma thread separada.
- **Condição de Sincronização**: Utiliza `threading.Condition` para coordenar o carregamento e descarregamento de encomendas.
- **Encerramento Sincronizado**: O programa aguarda todas as encomendas serem entregues antes de encerrar.

## Requisitos

- Python 3.9 ou superior
- Classes definidas nos seguintes arquivos:
  - `classes/caminhao.py`
  - `classes/encomenda.py`
  - `classes/centro_distribuicao.py`
  - `classes/entradas.py`

## Como Executar

1. Certifique-se de que os arquivos das classes mencionados acima estão no diretório correto.
2. Execute o script principal:
   ```bash
   python <nome_do_arquivo>.py
3. Durante a execução, o programa exibirá logs no terminal e salvará um histórico das encomendas no arquivo `rastro.txt`.

### Estrutura do Código

#### Threads

- **`encomenda_thread`**: Gerencia o transporte de uma encomenda, desde o carregamento até a entrega no centro de destino.
- **`caminhao_thread`**: Gerencia o trajeto de um caminhão, incluindo carregamento e descarregamento de encomendas nos centros de distribuição.

#### Bloco Principal

- Configura os parâmetros do ambiente com a classe `Entradas`.
- Inicializa centros de distribuição, caminhões e encomendas.
- Cria e inicia threads para cada caminhão e encomenda.
- Aguarda a finalização de todas as threads.

#### Classes Externas

- **`Caminhao`**: Representa os caminhões e sua lógica de transporte.
- **`Encomenda`**: Define os itens a serem transportados.
- **`CentroDistribuicao`**: Gerencia filas de caminhões e armazenamento de encomendas.
- **`Entradas`**: Fornece os parâmetros iniciais (quantidade de centros, caminhões, encomendas, etc.).

### Entradas e Saídas

#### Entradas

- **`S`**: Número de centros de distribuição.
- **`C`**: Número de caminhões.
- **`P`**: Número de encomendas.
- **`A`**: Capacidade de carga dos caminhões.

Os valores são fornecidos através da classe `Entradas`, que pode ser configurada para leitura interativa (`PROMPT`).

#### Saídas

**Exemplo de Logs no Terminal**:

```css 
Encomenda [1] adicionada ao centro de origem [0]
Caminhão [2] esperando no centro [3]
Encomenda [5] carregada no caminhão [2] no centro [3]
Encomenda [5] foi descarregada no centro de destino [1] pelo caminhão [2]
```


### Explicação do Código: `encomenda_thread`

A função `encomenda_thread` é responsável por gerenciar a trajetória de uma encomenda, desde sua adição ao centro de origem, o transporte via caminhão, até o descarregamento no centro de destino.

#### Parâmetros

- **`encomenda`**: Objeto da classe `Encomenda` que representa a encomenda a ser transportada.
- **`centros`**: Lista de objetos `CentroDistribuicao`, representando os centros de origem e destino.
- **`condition`**: Objeto `threading.Condition` para sincronização entre threads.
- **`all_delivered`**: Evento `threading.Event` que sinaliza quando todas as encomendas foram entregues.

---

### Etapas do Processo

#### 1. Identificação dos Centros de Origem e Destino

```python
centro_origem: CentroDistribuicao = centros[encomenda.origem]
centro_destino: CentroDistribuicao = centros[encomenda.destino]
```

A thread identifica os centros de distribuição de origem e destino com base nos índices da encomenda.


#### **2. Adicionar Encomenda ao Centro de Origem**
```python
with centro_origem.lock:
    centro_origem.adicionar_encomenda(encomenda, tempo_inicial)
    print(f"Encomenda [{encomenda.id}] adicionada ao centro de origem [{centro_origem.id}]")
```
- Um bloqueio (lock) é usado para garantir que a operação seja atômica, evitando conflitos entre threads.

- A encomenda é adicionada ao centro de origem pelo método adicionar_encomenda, que registra o horário inicial.


#### **3. Aguardar Transporte**
```python
with condition:
    print(f"Encomenda [{encomenda.id}] foi notificada para aguardar")
    while encomenda.id_caminhao is None:
        condition.wait()
```

- A função entra em uma seção crítica protegida pela condition.
- Se o campo id_caminhao da encomenda for None, significa que a encomenda ainda não foi atribuída a um caminhão, então a thread entra em espera com condition.wait() até que um caminhão seja atribuído.

#### **4. Simular Transporte**

```python
print(f"Encomenda [{encomenda.id}] está sendo transportada pelo caminhão [{encomenda.id_caminhao}]")
while encomenda.id_caminhao is not None:
    Caminhao.estrada()  # Simula o transporte na estrada
```

- Após a encomenda ser atribuída a um caminhão, a thread exibe uma mensagem indicando que a encomenda está em transporte. A função Caminhao.estrada() é chamada para simular o tempo que o caminhão levaria na estrada até o centro de destino.


#### **5. Verificar Entrega**
```python
for caminhao in caminhoes:
    if caminhao.id == encomenda.id_caminhao and caminhao.localizacao == centro_destino.id:
        centro_destino.remover_encomenda(encomenda)
        time.sleep(random.randint(1, 5))  # Simula o tempo de descarregamento
        encomenda.horario_despacho = int((time.time() - tempo_inicial) * 1000)
        encomenda.anotar_rastro()  # Registra o rastreio da encomenda
        caminhao.remover_encomenda(encomenda)
        encomenda.id_caminhao = None
```

- O código percorre a lista de caminhões e verifica se o caminhão responsável pela encomenda chegou ao centro de destino.
- Se o caminhão correto chegar ao centro de destino:

    1. A encomenda é removida do centro de destino.
    2. Um tempo aleatório de descarregamento é simulado com time.sleep(random.randint(1, 5)).
    3. O horário de despacho da encomenda é registrado em milissegundos a partir do tempo inicial.
    4. O rastreio da encomenda é atualizado com o método anotar_rastro().
    5. A encomenda é removida do caminhão e o id_caminhao é resetado para None.


#### **6. Notificar Threads**

```python
with condition:
    condition.notify_all()  # Notifica todas as threads aguardando a condição
print(f"Encomenda [{encomenda.id}] foi descarregada no centro de destino [{centro_destino.id}] pelo caminhão [{caminhao.id}]")
```

- Após a entrega da encomenda, a condition.notify_all() é chamada para notificar todas as threads que estavam aguardando a condição de que a encomenda foi entregue.
- Isso permite que outras threads possam continuar seu trabalho sem depender dessa entrega.
- Um log é impresso indicando que a encomenda foi descarregada no centro de destino e identificando o caminhão responsável pela entrega.

#### **Exemplos de log no terminal**

Durante a execução, o programa gera logs no terminal para monitoramento do transporte e entrega das encomendas, como no exemplo abaixo:

```css
Encomenda [1] foi notificada para aguardar
Encomenda [1] está sendo transportada pelo caminhão [2]
Encomenda [1] foi descarregada no centro de destino [3] pelo caminhão [2]
```

- Esses logs ajudam a acompanhar cada passo do processo, desde a notificação para aguardar até a entrega final da encomenda.



