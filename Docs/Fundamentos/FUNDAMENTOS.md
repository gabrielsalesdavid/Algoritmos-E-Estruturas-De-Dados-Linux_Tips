# Fundamentos de Python e estruturas de dados

Este material explica as construções usadas nos exemplos deste repositório. Os exemplos são didáticos; consulte o README principal para os pontos de atenção conhecidos antes de executá-los.

## 1. Instruções, nomes e atribuição

Uma instrução Python pode criar um valor, chamar uma função ou atribuir um resultado a um nome:

```python
quantidade = len([10, 20, 30])
print(quantidade)
```

- `quantidade` é um identificador que nomeia um objeto.
- `=` atribui a referência do valor à variável; não é o operador de igualdade.
- `len(...)` chama uma função e devolve o número de elementos.
- `print(...)` chama uma função para exibir valores.
- Parênteses agrupam argumentos de chamadas e podem definir precedência em expressões.

Python usa indentação para delimitar blocos. Depois de cabeçalhos como `if`, `for`, `while`, `class` e `def`, os dois-pontos `:` iniciam um bloco indentado.

## 2. Tipos de valores

Os exemplos usam:

- Inteiros, como `3`; números decimais, como `3.14`.
- Strings, como `"Python"` ou `'Python'`; ambas as formas delimitam texto.
- Booleanos `True` e `False`.
- `None`, que representa ausência de valor.
- Coleções, como listas, dicionários, conjuntos e `deque`.

`type(valor)` permite consultar o tipo do objeto. O tipo determina as operações disponíveis: por exemplo, listas têm `append()`, enquanto conjuntos têm `add()`.

## 3. Listas e índices

Uma lista é uma sequência mutável, escrita entre colchetes. Seus elementos são ordenados e podem se repetir:

```python
frutas = ["maçã", "pera", "uva"]
primeira = frutas[0]
ultima = frutas[-1]
```

Os índices começam em zero; `-1` acessa o último elemento. Acesso a um índice fora dos limites gera `IndexError`.

Operações demonstradas:

- `append(valor)`: inclui um valor ao final.
- `insert(indice, valor)`: insere em uma posição.
- `extend(iteravel)`: acrescenta cada elemento de outro iterável.
- `pop(indice)`: remove e devolve um elemento; sem índice, remove o último.
- `remove(valor)`: remove a primeira ocorrência do valor.
- `del lista[indice]`: remove pelo índice.
- `len(lista)`: informa o tamanho.
- `valor in lista`: testa se um valor pertence à lista.

Listas Python não têm `push()` como método. Para acrescentar ao final, use `append()`.

## 4. Conjuntos e dicionários

### Conjuntos (`set`)

Conjuntos são coleções mutáveis de elementos únicos, sem ordem de indexação. Literais usam chaves; para um conjunto vazio, use `set()` (e não `{}`, que cria um dicionário vazio).

- `add(valor)` inclui um elemento.
- `union(outro)` combina elementos.
- `intersection(outro)` obtém os elementos comuns.
- `difference(outro)` obtém os elementos que só estão no primeiro conjunto.
- `symmetric_difference(outro)` obtém os elementos que aparecem em apenas um dos conjuntos.
- `sorted(conjunto)` produz uma nova lista ordenada; `reverse=True` inverte a ordem crescente padrão.

### Dicionários (`dict`)

Dicionários associam chaves a valores. A sintaxe literal usa pares `chave: valor`:

```python
time = {"nome": "Time A", "cidade": "São Paulo"}
nome = time["nome"]
```

Colchetes com uma chave leem ou atualizam o valor correspondente. Para percorrer valores compostos, um `for` pode iterar uma lista de dicionários:

```python
times = [{"nome": "Time A"}, {"nome": "Time B"}]
for time in times:
    print(time["nome"])
```

Chaves de dicionário precisam ser hashable. Um dicionário (mutável) não pode ser usado como elemento de conjunto nem como chave de outro dicionário.

## 5. Condições e operadores

```python
if quantidade > 0:
    print("há elementos")
elif quantidade == 0:
    print("vazio")
else:
    print("valor negativo")
```

- `if` avalia a condição; `elif` testa uma condição alternativa; `else` cobre os demais casos.
- `==` compara igualdade; `!=` compara diferença.
- `<`, `<=`, `>` e `>=` comparam valores.
- `and` exige que ambas as condições sejam verdadeiras; `or` aceita uma delas; `not` inverte um valor lógico.
- `%` calcula o resto da divisão (por exemplo, `numero % 2 == 0` identifica um inteiro par).
- `+=` atualiza uma variável somando o valor à direita.

## 6. Laços e iteração

`for elemento in iteravel:` percorre os valores de uma sequência ou outro iterável. `range(inicio, limite, passo)` produz uma sequência de inteiros: o início é incluído, o limite é excluído e o passo é opcional. `input()` sempre devolve texto (`str`); converta para `int` ou `float` antes de fazer cálculos numéricos.

`while condição:` repete o bloco enquanto a condição for verdadeira. É importante atualizar o estado usado pela condição para evitar um laço infinito. `break` encerra o laço mais próximo; `return` encerra a função atual.

Laços podem ser aninhados, por exemplo, para percorrer linhas e colunas de uma matriz. A indentação mostra qual instrução pertence a cada laço ou condição.

## 7. Funções, métodos e classes

`def nome(parametros):` define uma função ou método. Quando definido dentro de uma classe, o primeiro parâmetro convencional é `self`, que referencia a instância que recebeu a chamada:

```python
class Exemplo:
    def __init__(self, valor):
        self.valor = valor

    def obter(self):
        return self.valor
```

- `class` declara um tipo de objeto.
- `__init__` é o método de inicialização chamado quando uma instância é criada; não é o próprio construtor que aloca o objeto.
- `self.valor = valor` guarda o argumento como atributo da instância.
- O ponto (`.`) acessa atributos e métodos, como `objeto.metodo()`.
- `return` devolve um resultado à chamada; se não há `return` explícito, a função retorna `None`.
- `raise Erro(...)` sinaliza uma exceção. `IndexError` indica, por exemplo, uma operação inválida por índice ou pilha vazia.

Métodos de lista como `append()` alteram o objeto existente e retornam `None`; não atribua o resultado de `append()` esperando obter a lista modificada.

## 8. Formatação e conversões

Uma f-string começa com `f` e permite interpolar expressões entre chaves:

```python
item = "uva"
print(f"Item: {item}")
```

`str(valor)` converte um valor para texto, útil ao concatenar números e strings. `print(..., end=" -> ")` substitui a quebra de linha padrão pelo texto indicado.

## 9. JSON e arquivos

O módulo padrão `json` converte entre texto JSON e objetos Python:

- `json.load(arquivo)` lê e interpreta JSON de um arquivo.
- `json.dump(objeto, arquivo, ensure_ascii=False, indent=4)` serializa um objeto para um arquivo.
- `open(caminho, modo, encoding=...)` abre um arquivo. O modo `'r'` lê; `'w'` cria ou sobrescreve.
- O objeto devolvido por `open()` é o arquivo e é nele que se chama `close()`. O objeto retornado por `json.load()` são os dados, não o arquivo.

Para código novo, um bloco `with open(...) as arquivo:` é preferível porque fecha o arquivo automaticamente ao sair do bloco.

O módulo `pathlib` ajuda a formar caminhos independentes do sistema operacional. Por exemplo, `Path(__file__).with_name("brasileirao.json")` localiza um arquivo ao lado do script atual. Isso evita depender da pasta em que o comando foi iniciado e de barras invertidas em strings.

## 10. Recursão e pilha de chamadas

Recursão acontece quando uma função chama a si mesma para resolver uma versão menor do problema. Toda recursão precisa de:

1. **Caso-base:** condição que encerra as chamadas.
2. **Caso recursivo:** chamada que aproxima a entrada do caso-base.

Por exemplo, `contagem_regressiva(n)` imprime `n` e chama `contagem_regressiva(n - 1)` até `n <= 0`. A cada chamada, o Python guarda o contexto na pilha de chamadas; quando o caso-base retorna, os contextos são removidos em ordem inversa. Se as chamadas não chegarem ao caso-base, o programa pode terminar com `RecursionError`.

Os exemplos `caso-base.py` e `caso-recursivo.py` mostram recursão com uma sequência de bonecas e uma árvore de departamentos. `pilha-de-chamads.py` mostra chamadas de funções encadeadas e a pilha de chamadas. Apesar do nome, `pilha-recursiva.py` consulta dicionários aninhados sem chamar a própria função; é um exemplo de acesso condicional a categorias.

## 11. Estruturas de dados do repositório

### Pilha (LIFO)

LIFO significa *Last In, First Out*: o último elemento inserido é o primeiro removido. O exemplo `src/PILHA E FILA/pilhas.py` guarda itens em `collections.deque`; `push()` acrescenta ao topo, `pop()` remove o topo e `peek()` consulta sem remover. A pasta menciona fila, mas ainda não há uma implementação de fila nos exemplos.

### Lista simplesmente ligada

Cada nó guarda um dado e uma referência `proximo`. A lista mantém uma `cabeca` para o primeiro nó. Para chegar ao final ou localizar um valor, é necessário percorrer as referências a partir da cabeça.

### Lista duplamente ligada

Cada nó guarda referências `proximo` e `anterior`. A lista também mantém `cabeca` e `cauda`, facilitando a inserção no final. Ao remover um nó, as referências dos vizinhos e as extremidades precisam ser atualizadas.

### Custos intuitivos das operações

| Estrutura/operação | Custo típico | Motivo |
| --- | --- | --- |
| Lista: acessar por índice | O(1) | A posição é calculada diretamente |
| Lista: buscar por valor | O(n) | Pode ser necessário examinar todos os itens |
| Lista: acrescentar no final | O(1) amortizado | `append()` geralmente acrescenta sem percorrer a lista |
| Conjunto: testar pertinência | O(1) médio | Usa hash; há casos de colisão |
| Pilha sobre `deque`: inserir/remover no topo | O(1) | Operações em uma extremidade |
| Lista ligada: buscar valor | O(n) | Percorre os nós sequencialmente |
| Lista simplesmente ligada: inserir no final | O(n) neste exemplo | Percorre do início porque não mantém referência de cauda |
| Lista duplamente ligada: inserir no final | O(1) neste exemplo | Usa a referência `cauda` |

`O(...)` descreve como o trabalho cresce com o tamanho dos dados, não o tempo exato de execução.

## 12. Mapa dos exemplos

- **Listas:** `src/LISTAS/listas.py`, `tamanho-listas.py`, `adicionar-elementos.py`, `remover.py`.
- **Laços e lógica:** `src/LISTAS/loop-for.py`, `operacoes-com-listas.py`, `adcionar.py`.
- **Matrizes:** `src/LISTAS/matrizes.py`.
- **Conjuntos:** `src/DICIONÁRIOS E SETS/sets.py`.
- **Dicionários e coleções combinadas:** `src/DICIONÁRIOS E SETS/dicionarios.py`, `dicioanrios-listas.py`.
- **JSON:** `src/DICIONÁRIOS E SETS/json-exemplo.py` e `brasileirao.json`.
- **Pilha:** `src/PILHA E FILA/pilhas.py`.
- **Listas ligadas:** `src/LISTAS LIGADAS/listas-simples-ligadas.py` e `listas-duplamente-ligadas.py`.
- **Recursão e chamadas:** `src/RECURSÃO/recursao.py`, `caso-base.py`, `caso-recursivo.py`, `pilha-de-chamads.py` e `pilha-recursiva.py`.

Comentários nos arquivos-fonte explicam a sintaxe e a intenção local de cada trecho; este documento reúne os conceitos e o contexto para estudo.
