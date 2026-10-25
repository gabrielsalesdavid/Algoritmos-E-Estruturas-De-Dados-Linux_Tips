# Fundamentos de Python e estruturas de dados

Este material explica as construções usadas nos exemplos deste repositório. Os exemplos são didáticos; consulte o README principal para os pontos de atenção conhecidos antes de executá-los.

## Como estudar este guia

Leia um tópico, copie o pequeno exemplo para um arquivo separado e altere um valor por vez. Antes de executar, tente prever o que será mostrado. Depois compare sua previsão com a saída. Assim fica mais fácil entender qual parte da sintaxe causou cada resultado.

Quando encontrar um nome como `frutas`, pense nele como uma etiqueta que permite encontrar um valor. Os parênteses `()` costumam aparecer em chamadas de funções e métodos; os colchetes `[]` criam listas ou acessam posições/chaves; as chaves `{}` criam conjuntos ou dicionários. A indentação (os espaços no começo da linha) mostra quais instruções pertencem a um bloco.

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

Leia `quantidade = len([10, 20, 30])` da direita para a esquerda: Python cria uma lista, conta seus três itens e guarda o resultado no nome `quantidade`. Se depois escrever `quantidade = quantidade + 1`, o nome passa a apontar para o novo resultado. O sinal `=` não pergunta se dois valores são iguais; para comparar, use `==`.

Em geral, um programa executa as instruções de cima para baixo. Uma condição ou um laço pode decidir se certas linhas serão executadas, quantas vezes serão repetidas ou se a execução seguirá por outro caminho.

## 2. Tipos de valores

Os exemplos usam:

- Inteiros, como `3`; números decimais, como `3.14`.
- Strings, como `"Python"` ou `'Python'`; ambas as formas delimitam texto.
- Booleanos `True` e `False`.
- `None`, que representa ausência de valor.
- Coleções, como listas, dicionários, conjuntos e `deque`.

`type(valor)` permite consultar o tipo do objeto. O tipo determina as operações disponíveis: por exemplo, listas têm `append()`, enquanto conjuntos têm `add()`.

O tipo também ajuda a explicar erros comuns. `"3"` é texto e `3` é um número inteiro: somar um texto e um número diretamente não é permitido. Use `int("3")` para obter o número, ou `str(3)` para obter texto. `float("3.5")` converte texto em número decimal. Se a pessoa digitar algo que não pode ser convertido, a conversão gera um erro; em programas maiores, valide a entrada antes de converter.

Python permite colocar tipos diferentes numa mesma lista, mas isso nem sempre deixa o programa fácil de entender. Quando os itens representam a mesma coisa, como uma lista de idades, prefira manter valores do mesmo tipo.

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

### Exemplo: mudar uma lista passo a passo

```python
frutas = ["maçã", "pera"]
frutas.append("uva")          # ["maçã", "pera", "uva"]
frutas.insert(1, "banana")    # ["maçã", "banana", "pera", "uva"]
frutas.extend(["kiwi", "manga"])
ultima = frutas.pop()         # remove e devolve "manga"
```

`append()` coloca um único objeto no final. `extend()` percorre outro iterável e acrescenta seus elementos. Por exemplo, `lista.append([1, 2])` coloca uma lista inteira como um elemento; `lista.extend([1, 2])` acrescenta dois elementos. `insert()` desloca os itens que vêm depois da posição. `pop()` é útil quando você precisa remover **e usar** o item retirado. `remove()` procura o valor e remove a primeira ocorrência; se o valor não existir, ocorre `ValueError`.

Para percorrer uma lista sem precisar dos números das posições, use `for fruta in frutas:`. Se também precisar da posição, `enumerate(frutas)` fornece a posição e o item. Em geral, isso é mais claro do que criar `range(len(frutas))`.

Uma lista pode guardar outras listas. Esse formato ajuda a representar uma tabela ou tabuleiro. Em `tabuleiro[linha][coluna]`, o primeiro índice escolhe a linha; o segundo escolhe a coluna. Como a contagem começa em zero, `tabuleiro[0][0]` representa a primeira célula.

## 4. Conjuntos e dicionários

### Conjuntos (`set`)

Conjuntos são coleções mutáveis de elementos únicos, sem ordem de indexação. Literais usam chaves; para um conjunto vazio, use `set()` (e não `{}`, que cria um dicionário vazio).

- `add(valor)` inclui um elemento.
- `union(outro)` combina elementos.
- `intersection(outro)` obtém os elementos comuns.
- `difference(outro)` obtém os elementos que só estão no primeiro conjunto.
- `symmetric_difference(outro)` obtém os elementos que aparecem em apenas um dos conjuntos.
- `sorted(conjunto)` produz uma nova lista ordenada; `reverse=True` inverte a ordem crescente padrão.

Conjuntos são úteis quando queremos saber se algo já apareceu, tirar duplicatas ou comparar grupos. Por exemplo, `{1, 2, 2, 3}` guarda apenas `{1, 2, 3}`. Como não há posições, `meu_conjunto[0]` não é uma forma válida de acessar um item. A ordem mostrada por `print()` não deve ser usada como critério.

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

Pense num dicionário como uma ficha: a chave identifica a informação e o valor contém essa informação. `time["nome"]` lê o valor; `time["cidade"] = "Recife"` cria ou substitui uma chave. Se uma chave pode estar ausente, `time.get("estadio", "não informado")` devolve uma alternativa sem gerar `KeyError`.

É comum guardar várias fichas em uma lista:

```python
times = [
    {"nome": "Time A", "cidade": "São Paulo"},
    {"nome": "Time B", "cidade": "Rio de Janeiro"},
]
for time in times:
    print(f"{time['nome']} joga em {time['cidade']}")
```

Os colchetes mais internos pertencem às chaves do dicionário; as chaves `{}` dentro da f-string indicam onde o valor será inserido no texto.

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

Uma comparação produz `True` ou `False`. O bloco de `if` só é executado quando sua condição resulta em `True`; `elif` permite verificar outra possibilidade e `else` cobre o que restou. A ordem importa: assim que uma condição verdadeira é encontrada, os blocos seguintes dessa cadeia não são executados.

Use `and` quando todas as regras precisam ser verdadeiras, por exemplo `idade >= 18 and tem_ingresso`. Use `or` quando basta uma regra, por exemplo `dia == "sábado" or dia == "domingo"`. Parênteses podem tornar expressões longas mais fáceis de ler.

## 6. Laços e iteração

`for elemento in iteravel:` percorre os valores de uma sequência ou outro iterável. `range(inicio, limite, passo)` produz uma sequência de inteiros: o início é incluído, o limite é excluído e o passo é opcional. `input()` sempre devolve texto (`str`); converta para `int` ou `float` antes de fazer cálculos numéricos.

`while condição:` repete o bloco enquanto a condição for verdadeira. É importante atualizar o estado usado pela condição para evitar um laço infinito. `break` encerra o laço mais próximo; `return` encerra a função atual.

Laços podem ser aninhados, por exemplo, para percorrer linhas e colunas de uma matriz. A indentação mostra qual instrução pertence a cada laço ou condição.

Use `for` quando há um conjunto de itens a percorrer ou quando a quantidade de repetições já é conhecida. Use `while` quando a repetição depende de uma condição que pode mudar, como esperar a pessoa digitar um valor de saída. Em todo `while`, verifique como a condição vai deixar de ser verdadeira; se nada a alterar, o programa pode repetir para sempre.

`break` sai imediatamente do laço mais próximo. `continue` pula o restante da repetição atual e começa a próxima. Evite usar esses comandos sem necessidade: uma condição clara muitas vezes deixa o fluxo mais fácil de acompanhar.

Uma compreensão de lista reúne criação, percurso e filtro numa expressão:

```python
numeros = [1, 2, 3, 4]
pares = [numero for numero in numeros if numero % 2 == 0]
```

O resultado é uma **lista nova** (`[2, 4]`); a lista `numeros` continua igual. Para quem está começando, escrever primeiro o `for` tradicional pode ajudar a enxergar os mesmos passos.

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

Uma função ajuda a dar nome a uma tarefa e permite reaproveitá-la:

```python
def calcular_dobro(numero):
    resultado = numero * 2
    return resultado

print(calcular_dobro(4))  # 8
```

`numero` é um parâmetro: o nome que a função usa para receber um valor. `4` é o argumento passado nessa chamada. `return` envia o resultado de volta a quem chamou a função; `print()` apenas mostra algo na tela e não substitui `return`.

Uma classe reúne dados e ações que pertencem a um mesmo tipo de objeto. Cada objeto criado a partir dela é uma instância. Dentro de um método, `self` é a própria instância que recebeu a chamada. Por isso, `self.valor` pertence àquele objeto e pode ser diferente em outra instância.

Por exemplo, uma pilha pode guardar os itens em `self.items` e oferecer métodos como `push()` e `pop()`. O método não é uma palavra especial: é uma função definida dentro de uma classe e chamada através de um objeto, como `minha_pilha.push(10)`.

## 8. Formatação e conversões

Uma f-string começa com `f` e permite interpolar expressões entre chaves:

```python
item = "uva"
print(f"Item: {item}")
```

`str(valor)` converte um valor para texto, útil ao concatenar números e strings. `print(..., end=" -> ")` substitui a quebra de linha padrão pelo texto indicado.

F-strings deixam claro onde cada informação será colocada. `f"Item: {item}"` incorpora o conteúdo de `item`; expressões simples também podem aparecer entre as chaves, como `f"Total: {preco * quantidade:.2f}"`. O trecho `:.2f` mostra um número decimal com duas casas, útil no exemplo de preço do carrinho.

## 9. JSON e arquivos

O módulo padrão `json` converte entre texto JSON e objetos Python:

- `json.load(arquivo)` lê e interpreta JSON de um arquivo.
- `json.dump(objeto, arquivo, ensure_ascii=False, indent=4)` serializa um objeto para um arquivo.
- `open(caminho, modo, encoding=...)` abre um arquivo. O modo `'r'` lê; `'w'` cria ou sobrescreve.
- O objeto devolvido por `open()` é o arquivo e é nele que se chama `close()`. O objeto retornado por `json.load()` são os dados, não o arquivo.

Para código novo, um bloco `with open(...) as arquivo:` é preferível porque fecha o arquivo automaticamente ao sair do bloco.

O módulo `pathlib` ajuda a formar caminhos independentes do sistema operacional. Por exemplo, `Path(__file__).with_name("brasileirao.json")` localiza um arquivo ao lado do script atual. Isso evita depender da pasta em que o comando foi iniciado e de barras invertidas em strings.

JSON é um formato de texto para guardar dados estruturados. Um objeto JSON com chaves e valores vira normalmente um dicionário Python; uma lista JSON vira uma lista Python. `json.load()` faz essa leitura e `json.dump()` faz o caminho inverso. Os dados precisam ter tipos que JSON consegue representar, como texto, números, valores lógicos, listas, dicionários e `None`.

O modo `'w'` substitui o conteúdo anterior do arquivo. Antes de executar o exercício JSON, faça uma cópia do arquivo de dados se quiser conservá-lo. O modo `'r'` serve para leitura e `'a'` acrescenta texto ao final, embora acrescentar JSON dessa forma nem sempre produza um documento JSON válido.

`with` abre um bloco de uso do arquivo e fecha o arquivo automaticamente quando o bloco termina, inclusive se ocorrer um erro. É mais seguro do que depender de uma chamada manual a `close()`.

## 10. Recursão e pilha de chamadas

Recursão acontece quando uma função chama a si mesma para resolver uma versão menor do problema. Toda recursão precisa de:

1. **Caso-base:** condição que encerra as chamadas.
2. **Caso recursivo:** chamada que aproxima a entrada do caso-base.

Por exemplo, `contagem_regressiva(n)` imprime `n` e chama `contagem_regressiva(n - 1)` até `n <= 0`. A cada chamada, o Python guarda o contexto na pilha de chamadas; quando o caso-base retorna, os contextos são removidos em ordem inversa. Se as chamadas não chegarem ao caso-base, o programa pode terminar com `RecursionError`.

Os exemplos `caso-base.py` e `caso-recursivo.py` mostram recursão com uma sequência de bonecas e uma árvore de departamentos. `pilha-de-chamads.py` mostra chamadas de funções encadeadas e a pilha de chamadas. Apesar do nome, `pilha-recursiva.py` consulta dicionários aninhados sem chamar a própria função; é um exemplo de acesso condicional a categorias.

Na contagem regressiva, a primeira chamada começa com `5`; depois vêm chamadas com `4`, `3`, `2`, `1` e `0`. Quando chega a `0`, o caso-base imprime a mensagem final e não faz outra chamada. Assim, as chamadas terminam. Uma função que chama a si mesma com o mesmo valor e sem uma condição de parada não progride e pode acabar em `RecursionError`.

Recursão é uma forma de organizar a solução, não a única forma de resolver um problema. Para percursos muito longos, um laço pode usar menos espaço e ser mais adequado. O objetivo dos exemplos é mostrar o funcionamento, não recomendar recursão para todo caso.

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

Para comparar a ideia, imagine procurar um nome numa lista sem ordem: no pior caso será preciso conferir um por um, então o trabalho cresce junto com a quantidade de nomes (O(n)). Se a quantidade dobrar, o número de verificações também pode aproximadamente dobrar. Acesso por índice numa lista vai direto à posição solicitada (O(1)); a quantidade de itens não faz o número de passos desse acesso crescer da mesma maneira.

Dois laços um dentro do outro podem comparar cada item de uma lista com cada item de outra. Se ambas tiverem `n` itens, o número de comparações pode se aproximar de `n × n`, ou O(n²). Isso não significa que todo laço duplo seja automaticamente lento; significa que é importante notar quantas repetições acontecem conforme os dados aumentam.

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
