<div align="center">

# 🐍 Algoritmos e Estruturas de Dados com Python

**Um espaço de estudos práticos para aprender Python e entender como os dados se organizam.**

Exemplos comentados • conceitos fundamentais • estruturas de dados

<br>

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Foco](https://img.shields.io/badge/foco-aprendizado%20pr%C3%A1tico-2ea44f)
![Idioma](https://img.shields.io/badge/documenta%C3%A7%C3%A3o-Portugu%C3%AAs-8250df)

</div>

---

## 👋 Sobre o projeto

Este repositório reúne exercícios introdutórios de **Python**, **algoritmos** e **estruturas de dados**. A proposta é aprender pela leitura e experimentação: cada exemplo mostra uma ideia pequena, e os comentários no código ajudam a entender a sintaxe, as operações e a lógica utilizada.

É um projeto de estudos em evolução — não um pacote pronto para produção. Alguns exercícios ainda têm limitações conhecidas, que estão descritas com transparência neste README para que iniciantes possam reconhecê-las e praticar a correção.

## 📖 O que você vai aprender, explicado com calma

Este material foi pensado para quem está começando. Não é necessário conhecer os nomes técnicos antes de abrir os exemplos: a ideia é observar uma situação simples, ver como Python a representa e, então, praticar.

| Tema | Em palavras simples | Onde praticar |
| --- | --- | --- |
| **Variáveis e valores** | Dar um nome a um dado, como `idade = 20`, para poder usá-lo depois. Números, textos e valores verdadeiro/falso têm tipos diferentes. | [Exemplo de listas e tipos](src/LISTAS/listas.py) |
| **Listas e posições** | Guardar vários itens em ordem. A primeira posição é `0`; por isso, o terceiro item fica no índice `2`. | [Índices](src/LISTAS/listas.py), [tamanho](src/LISTAS/tamanho-listas.py), [adicionar](src/LISTAS/adicionar-elementos.py), [remover](src/LISTAS/remover.py) |
| **Condições** | Fazer o programa escolher o que fazer: por exemplo, mostrar uma mensagem diferente se a lista estiver vazia. | [Operações com listas](src/LISTAS/operacoes-com-listas.py), [carrinho interativo](src/LISTAS/adcionar.py) |
| **Repetições** | Repetir uma ação para cada item (`for`) ou enquanto uma regra continuar verdadeira (`while`). | [Laço `for`](src/LISTAS/loop-for.py), [tamanho e `while`](src/LISTAS/tamanho-listas.py) |
| **Listas e matrizes** | Uma lista pode conter outras listas, como linhas e colunas de um tabuleiro ou de uma tabela. | [Matrizes](src/LISTAS/matrizes.py) |
| **Conjuntos** | Guardar valores sem repeti-los e comparar grupos, por exemplo para encontrar elementos comuns. | [Conjuntos (`set`)](<src/DICIONÁRIOS E SETS/sets.py>) |
| **Dicionários** | Guardar informações com rótulos: `"nome"` aponta para um nome, `"cidade"` aponta para uma cidade. | [Dicionários em listas](<src/DICIONÁRIOS E SETS/dicioanrios-listas.py>) |
| **JSON e arquivos** | Ler dados guardados em um arquivo, trabalhar com eles como listas e dicionários e gravar mudanças. | [Exemplo JSON](<src/DICIONÁRIOS E SETS/json-exemplo.py>) |
| **Pilha** | Guardar itens de modo que o último colocado seja o primeiro a sair, como pratos empilhados. | [Pilha LIFO](<src/PILHA E FILA/pilhas.py>) |
| **Listas ligadas** | Conectar elementos por referências; cada elemento sabe onde está o próximo (e, na versão dupla, o anterior). | [Lista simples](<src/LISTAS LIGADAS/listas-simples-ligadas.py>), [lista dupla](<src/LISTAS LIGADAS/listas-duplamente-ligadas.py>) |
| **Recursão** | Resolver uma tarefa com chamadas menores da mesma função até chegar a uma condição que manda parar. | [Contagem regressiva](<src/RECURSÃO/recursao.py>), [departamentos](<src/RECURSÃO/caso-recursivo.py>) |
| **Crescimento do trabalho** | Comparar se uma tarefa continua simples ou exige cada vez mais passos conforme a quantidade de dados aumenta. | [Guia de conceitos](Docs/Conceitos/CONCEITOS.md#6-notação-o) |

### As ideias em imagens

As figuras abaixo são desenhos originais deste repositório para explicar as ideias sem exigir que a pessoa já conheça os termos:

![Escolha entre lista, conjunto e dicionário](Docs/Conceitos/img/escolha-colecao.svg)

![Passo a passo da recursão com contagem regressiva](Docs/Conceitos/img/recursao-passo-a-passo.svg)

![Como os dados passam do arquivo JSON para Python e de volta](Docs/Conceitos/img/leitura-json.svg)

As figuras de [índices](Docs/Conceitos/img/lista-indices.svg), [listas ligadas](Docs/Conceitos/img/listas-ligadas.svg) e [pilha](Docs/Conceitos/img/pilha-lifo.svg) complementam os exemplos correspondentes.

### O que você vai encontrar

| Fundamentos de Python | Estruturas de dados |
| --- | --- |
| Variáveis, tipos e operadores | Listas e matrizes |
| Condições e laços `for` / `while` | Conjuntos e dicionários |
| Funções, classes, métodos e `self` | Pilha LIFO com `deque` |
| Recursão, pilha de chamadas e f-strings | Listas simplesmente e duplamente ligadas |
| Arquivos e módulo `json` | Busca, inserção e remoção |

## 🧭 Trilha de aprendizagem

Uma ordem sugerida para explorar o conteúdo:

1. **Conheça as sequências:** [listas e índices](src/LISTAS/listas.py), [tamanho](src/LISTAS/tamanho-listas.py), [adição](src/LISTAS/adicionar-elementos.py) e [remoção](src/LISTAS/remover.py).
2. **Pratique a lógica:** [laço `for`](src/LISTAS/loop-for.py), [operações e filtros](src/LISTAS/operacoes-com-listas.py), [matrizes](src/LISTAS/matrizes.py) e [entrada interativa](src/LISTAS/adcionar.py).
3. **Explore coleções:** [conjuntos (`set`)](src/DICION%C3%81RIOS%20E%20SETS/sets.py), [dicionários](src/DICION%C3%81RIOS%20E%20SETS/dicionarios.py), [listas de dicionários](src/DICION%C3%81RIOS%20E%20SETS/dicioanrios-listas.py) e [JSON](<src/DICIONÁRIOS E SETS/json-exemplo.py>).
4. **Entenda estruturas ligadas e pilhas:** [pilha LIFO](<src/PILHA E FILA/pilhas.py>), [lista simplesmente ligada](<src/LISTAS LIGADAS/listas-simples-ligadas.py>) e [lista duplamente ligada](<src/LISTAS LIGADAS/listas-duplamente-ligadas.py>).
5. **Explore recursão:** [contagem regressiva](<src/RECURSÃO/recursao.py>), [caso-base](<src/RECURSÃO/caso-base.py>), [árvore de departamentos](<src/RECURSÃO/caso-recursivo.py>) e [pilha de chamadas](<src/RECURSÃO/pilha-de-chamads.py>).
6. **Aprofunde os conceitos:** consulte [Fundamentos de Python e estruturas de dados](Docs/Fundamentos/FUNDAMENTOS.md), [Conceitos de algoritmos e estruturas de dados](Docs/Conceitos/CONCEITOS.md) e os diagramas visuais.

> **Dica para iniciantes:** leia primeiro os comentários, execute um exemplo por vez e experimente alterar os dados de entrada. Quando um arquivo tiver uma limitação conhecida, consulte [Antes de executar todos os exemplos](#-antes-de-executar-todos-os-exemplos).

### Como escolher uma coleção ou estrutura

Cada estrutura organiza os dados de um jeito diferente. A escolha depende do tipo de operação que o programa precisa realizar com mais frequência:

| Estrutura | Como organiza os dados | Quando é útil | Atenção |
| --- | --- | --- | --- |
| **Lista (`list`)** | Mantém os itens em sequência e permite repetições. Cada item pode ser acessado por um índice. | Guardar uma coleção ordenada, percorrer itens ou alterar uma posição. | Os índices começam em `0`. Procurar um valor que não está em uma posição conhecida exige percorrer a lista. |
| **Conjunto (`set`)** | Mantém elementos únicos, sem uma posição fixa para cada item. | Remover duplicatas, verificar pertencimento ou comparar grupos com união e interseção. | Não use um conjunto quando a posição ou a repetição dos itens for importante. |
| **Dicionário (`dict`)** | Associa uma chave a um valor, como `"nome"` a `"Ana"`. | Consultar informações por um identificador, como o nome de uma propriedade. | As chaves precisam ser únicas e hashable (por exemplo, textos e números; listas não podem ser usadas como chaves). |
| **Lista ligada** | Cada nó guarda um valor e uma referência para outro nó; na versão dupla, também guarda a referência anterior. | Estudar como conexões entre elementos podem ser representadas e percorridas. | É uma estrutura implementada nos exemplos para fins didáticos; listas Python já oferecem operações próprias para uso cotidiano. |
| **Pilha** | Segue a regra LIFO: o último item inserido é o primeiro removido. | Modelar ações como desfazer operações ou acompanhar chamadas de funções. | O exemplo usa `deque` como base e apresenta operações de pilha; ele não implementa uma fila. |

Uma forma simples de decidir é perguntar: **preciso de posições, de itens únicos ou de uma consulta por chave?** Para posições, considere uma lista; para unicidade e operações entre grupos, um conjunto; para relacionar identificadores e informações, um dicionário. Pilhas e listas ligadas aparecem nos exemplos para explorar regras e referências específicas.

### Como interpretar a eficiência de um algoritmo

A notação **O (Big O)** descreve como o trabalho de um algoritmo tende a crescer quando aumenta a quantidade de dados. Ela não é uma medida de segundos: o tempo real também depende do computador, da linguagem, da implementação e dos dados de entrada.

| Notação | Ideia aproximada | Exemplo de situação |
| --- | --- | --- |
| **O(1)** | O número de passos permanece aproximadamente constante quando a coleção cresce. | Acessar uma posição conhecida de uma lista. |
| **O(log n)** | O trabalho cresce lentamente porque, a cada etapa, o espaço de busca pode ser reduzido. | Uma busca que divide repetidamente um conjunto ordenado ao meio. |
| **O(n)** | O trabalho cresce junto com a quantidade de itens. | Percorrer uma lista inteira para procurar um valor. |
| **O(n²)** | O trabalho pode crescer proporcionalmente ao quadrado da quantidade de itens. | Comparar cada item com todos os demais usando dois laços aninhados. |

Essas situações são exemplos conceituais, não uma classificação automática de todos os arquivos deste repositório. A notação depende da operação analisada e das condições do algoritmo: por exemplo, a busca que reduz o espaço pela metade pressupõe dados ordenados e uma implementação adequada.

## 🗺️ Organização do repositório

```text
.
├── README.md
├── Docs/
│   ├── Conceitos/
│   │   ├── CONCEITOS.md         # Estruturas, recursão e notação O
│   │   └── img/                 # Diagramas conceituais em SVG
│   └── Fundamentos/
│       └── FUNDAMENTOS.md       # Guia de sintaxe e estruturas
└── src/
    ├── DICIONÁRIOS E SETS/      # set, dict, JSON e dados de exemplo
    ├── LISTAS/                  # listas, matrizes, iteração e operações
    ├── LISTAS LIGADAS/          # listas simplesmente e duplamente ligadas
    ├── PILHA E FILA/            # exemplo de pilha com deque
    └── RECURSÃO/                # casos-base, recursão e chamadas de funções
```

### Índice completo dos exemplos

<details>
<summary><strong>Listas, matrizes e controle de fluxo</strong></summary>

| Exemplo | Conceitos |
| --- | --- |
| [`listas.py`](src/LISTAS/listas.py) | Listas, tipos, índices, `print()`, f-strings e `type()` |
| [`tamanho-listas.py`](src/LISTAS/tamanho-listas.py) | `len()`, índices e `while` |
| [`adicionar-elementos.py`](src/LISTAS/adicionar-elementos.py) | `append()`, `insert()` e `extend()` |
| [`remover.py`](src/LISTAS/remover.py) | `del`, `pop()`, `remove()`, `in` e `while` |
| [`loop-for.py`](src/LISTAS/loop-for.py) | Laço `for` e `range()` |
| [`operacoes-com-listas.py`](src/LISTAS/operacoes-com-listas.py) | Compreensão de listas, filtros, operadores e laços aninhados |
| [`matrizes.py`](src/LISTAS/matrizes.py) | Listas de listas e índices de linha/coluna |
| [`adcionar.py`](src/LISTAS/adcionar.py) | Entrada do usuário, condições, `break` e recibo |

</details>

<details>
<summary><strong>Conjuntos, dicionários e JSON</strong></summary>

| Exemplo | Conceitos |
| --- | --- |
| [`sets.py`](<src/DICIONÁRIOS E SETS/sets.py>) | Conjuntos, união, interseção e diferenças |
| [`dicionarios.py`](<src/DICIONÁRIOS E SETS/dicionarios.py>) | Dicionários e acesso por chave |
| [`dicioanrios-listas.py`](<src/DICIONÁRIOS E SETS/dicioanrios-listas.py>) | Lista de dicionários, iteração e f-strings |
| [`json-exemplo.py`](<src/DICIONÁRIOS E SETS/json-exemplo.py>) | Leitura e gravação de dados JSON com `pathlib` |
| [`brasileirao.json`](<src/DICIONÁRIOS E SETS/brasileirao.json>) | Dados usados pelo exercício de JSON |

</details>

<details>
<summary><strong>Pilhas e listas ligadas</strong></summary>

| Exemplo | Conceitos |
| --- | --- |
| [`pilhas.py`](<src/PILHA E FILA/pilhas.py>) | Classe, `__init__`, `self`, métodos e pilha LIFO com `deque` |
| [`listas-simples-ligadas.py`](<src/LISTAS LIGADAS/listas-simples-ligadas.py>) | Nós, referências, busca, inserção e remoção |
| [`listas-duplamente-ligadas.py`](<src/LISTAS LIGADAS/listas-duplamente-ligadas.py>) | Referências anterior/próximo, cabeça e cauda |

</details>

<details>
<summary><strong>Recursão e chamadas de funções</strong></summary>

| Exemplo | Conceitos |
| --- | --- |
| [`recursao.py`](<src/RECURSÃO/recursao.py>) | Caso-base e contagem regressiva |
| [`caso-base.py`](<src/RECURSÃO/caso-base.py>) | Redução da entrada até a condição de parada |
| [`caso-recursivo.py`](<src/RECURSÃO/caso-recursivo.py>) | Percurso recursivo de uma árvore de departamentos |
| [`pilha-de-chamads.py`](<src/RECURSÃO/pilha-de-chamads.py>) | Funções encadeadas e pilha de chamadas |
| [`pilha-recursiva.py`](<src/RECURSÃO/pilha-recursiva.py>) | Dicionários aninhados e consulta de categoria; não usa recursão |

</details>

## 🖼️ Conceitos em imagens

Os diagramas são **ilustrações conceituais** das estruturas, não capturas de tela de programas em execução.

<details>
<summary><strong>Ver diagrama da pilha (LIFO)</strong></summary>
<br>

![Diagrama conceitual de pilha: push e pop](Docs/Conceitos/img/pilha-lifo.svg)

</details>

<details>
<summary><strong>Ver diagrama das listas ligadas</strong></summary>
<br>

![Comparação conceitual de listas simplesmente e duplamente ligadas](Docs/Conceitos/img/listas-ligadas.svg)

</details>

<details>
<summary><strong>Ver diagrama dos índices de uma lista</strong></summary>
<br>

![Diagrama conceitual dos índices de uma lista Python](Docs/Conceitos/img/lista-indices.svg)

</details>

## 🚀 Comece a praticar

### Requisitos

- Python 3 instalado.
- Terminal aberto na pasta raiz do repositório.
- Não há dependências externas declaradas para os exemplos documentados. O código usa módulos da biblioteca padrão, como `collections` e `json`.

### Executar um exemplo

No PowerShell:

```powershell
python --version
python "src\LISTAS\loop-for.py"
```

Outro exemplo, que demonstra uma classe de pilha:

```powershell
python "src\PILHA E FILA\pilhas.py"
```

Execute **um arquivo por vez**: cada exercício é independente. O exemplo [`adcionar.py`](src/LISTAS/adcionar.py) pede que você digite produtos no terminal; informe `0` para encerrar a entrada.

## ⚠️ Antes de executar todos os exemplos

Os exemplos refletem o estado atual do material de estudo. Alguns contêm trechos incompletos ou erros conhecidos; os avisos abaixo servem para evitar confusão ao executar:

| Arquivo | O que observar |
| --- | --- |
| [`dicionarios.py`](<src/DICIONÁRIOS E SETS/dicionarios.py>) | O literal tenta usar dicionários dentro de um conjunto. Dicionários são mutáveis e não podem ser elementos de um conjunto; a expressão falha antes do acesso por chave. |
| [`json-exemplo.py`](<src/DICIONÁRIOS E SETS/json-exemplo.py>) | O exemplo atualiza os títulos do Palmeiras e grava o resultado no JSON de exemplo. A operação pode ser repetida sem duplicar o novo título, mas altera o arquivo; faça uma cópia se quiser preservar os dados originais. |
| [`adicionar-elementos.py`](src/LISTAS/adicionar-elementos.py) | Listas não têm método `push()`. A chamada gera `AttributeError` e interrompe o script nesse ponto. |
| [`tamanho-listas.py`](src/LISTAS/tamanho-listas.py) | `i` não é inicializada e `t_numeros` é um inteiro; portanto, o acesso `t_numeros[i]` não funciona. |
| [`sets.py`](<src/DICIONÁRIOS E SETS/sets.py>) | Os nomes `ordered_ascending`/`ordered_descending` não correspondem aos valores de `reverse`: `True` indica ordem reversa (decrescente). |

Os exercícios ainda têm limitações descritas acima; execute somente depois de entendê-las. O exemplo JSON grava os dados que modifica, então preserve uma cópia se necessário.

## 📚 Documentação

- **[Fundamentos de Python e estruturas de dados](Docs/Fundamentos/FUNDAMENTOS.md):** guia passo a passo de nomes e valores, tipos, listas, conjuntos, dicionários, condições, repetições, funções, classes, arquivos JSON, recursão, pilhas e crescimento do trabalho.
- **[Conceitos de algoritmos e estruturas de dados](Docs/Conceitos/CONCEITOS.md):** explica em linguagem simples como escolher coleções, como listas ligadas guardam conexões, como funcionam pilhas e filas, o que acontece durante a recursão e como entender O(1), O(n), O(n²) e O(log n).
- **Comentários no código:** os 20 arquivos `.py` em `src/` incluem explicações em português das sintaxes e operações estudadas.
- **Diagramas:** os SVGs em `Docs/Conceitos/img/` ilustram índices, coleções, listas ligadas, pilhas, recursão e leitura/gravação JSON.

## 🔗 Como os assuntos se conectam

Os tópicos do repositório formam uma sequência: primeiro, os valores são guardados em coleções; depois, o programa percorre e transforma esses dados; por fim, diferentes estruturas e estratégias mostram maneiras de organizar ou processar as informações.

1. **Dados e coleções:** listas, conjuntos e dicionários oferecem formas diferentes de guardar valores. Entender suas diferenças ajuda a escolher como representar uma situação.
2. **Algoritmos sobre coleções:** condições e repetições permitem selecionar, contar e transformar os itens. Índices e tamanho ajudam a controlar o acesso sem ultrapassar os limites da lista.
3. **Estruturas com regras próprias:** pilhas e listas ligadas demonstram como operações e referências determinam a forma de inserir, localizar e remover elementos.
4. **Recursão:** uma função divide a tarefa em chamadas menores. O caso-base define quando parar, e as chamadas pendentes ficam registradas na pilha de chamadas.
5. **Eficiência:** a notação O ajuda a discutir como o trabalho muda com a quantidade de dados. Ela complementa a leitura do código, mas não substitui a análise da operação específica.

Ao comparar uma lista Python com uma lista ligada, por exemplo, observe que ambas podem representar uma sequência, mas guardam e percorrem seus elementos de maneiras diferentes. Uma pilha, por sua vez, descreve uma regra de uso — inserir e remover pelo topo — e pode ser construída sobre outra estrutura, como o `deque` usado no exemplo.

## 🧪 Um método para estudar cada exemplo

Para transformar a leitura em prática, experimente seguir estes passos em cada arquivo:

1. **Leia o objetivo e os comentários.** Identifique quais dados entram, qual operação será demonstrada e o que o programa deve mostrar.
2. **Preveja o resultado.** Antes de executar, anote a saída esperada ou o estado que a coleção terá depois de cada operação.
3. **Execute somente aquele arquivo.** Use os comandos da seção [Comece a praticar](#-comece-a-praticar) e observe a saída no terminal.
4. **Altere uma coisa de cada vez.** Troque valores, acrescente um item ou mude uma condição; execute novamente para descobrir como isso afeta o resultado.
5. **Explique o comportamento com suas palavras.** Pergunte-se por que o índice começa em zero, qual condição encerra o laço ou o que acontece quando uma pilha fica vazia.

Se a saída não for a prevista, compare o estado dos dados antes e depois de cada linha relevante. Esse processo ajuda a localizar a operação que mudou o resultado e é mais informativo do que executar todos os exemplos ao mesmo tempo.

As mudanças de código foram verificadas com compilação dos arquivos Python e testes dos exemplos da pilha e JSON. O JSON de exemplo foi testado usando cópias temporárias para preservar o arquivo original.

### Verificação de sintaxe

Os arquivos Python foram compilados com Python 3.12 para verificar a sintaxe (`python -m compileall -q src`). A compilação não executa os exemplos nem garante que todos funcionem: consulte a tabela de limitações acima antes de rodá-los.

## 🎯 Objetivos de aprendizagem

Ao explorar os exemplos, a pessoa iniciante pode praticar como:

- Ler e escrever sintaxe Python básica, com indentação, variáveis, expressões e chamadas.
- Usar coleções e escolher entre sequência, conjunto e dicionário.
- Percorrer dados com laços e filtrá-los com condições.
- Representar estruturas de dados com nós e referências.
- Relacionar o código a diagramas e explicar operações de inserção, busca e remoção.

---

<div align="center">

Feito para estudar, experimentar e aprender um conceito de cada vez. 🌱

</div>
