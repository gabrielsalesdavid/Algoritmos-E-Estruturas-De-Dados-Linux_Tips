# ====================================== SETS ======================================

# Chaves criam um conjunto (set); seus elementos são únicos e não têm ordem fixa.
frutas = {"maçã", "banana", "laranja", "uva"}
print(frutas)  # Chama print() para exibir o valor no terminal.

# set() constrói um conjunto vazio; {} sozinho criaria um dicionário vazio.
frutas = set()
print(frutas)

frutas.add("pera")  # Ponto acessa o método add, que inclui um elemento no conjunto.
print(frutas)

# A chamada union() combina conjuntos e devolve outro conjunto.
union = frutas.union({"abacaxi", "manga"})
print(union)

# sorted() recebe um iterável e devolve uma nova lista ordenada.
sorted_frutas = sorted(frutas)
print(sorted_frutas)

# Argumentos nomeados usam o formato nome=valor; reverse=True inverte a ordenação.
ordered_ascending = sorted(frutas, reverse=True)
ordered_descending = sorted(frutas, reverse=False)
print(ordered_ascending)
print(ordered_descending)

# intersection() retorna os elementos comuns aos dois conjuntos.
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {4, 5, 6, 7, 8}
intersecao = conjunto1.intersection(conjunto2)
print(intersecao)  # Exibe {4, 5}.

# difference() retorna elementos do primeiro conjunto que não estão no segundo.
diferenca = conjunto1.difference(conjunto2)
print(diferenca)  # Exibe {1, 2, 3}.

# symmetric_difference() retorna elementos presentes em apenas um dos conjuntos.
diferenca_simetrica = conjunto1.symmetric_difference(conjunto2)
print(diferenca_simetrica)  # Exibe {1, 2, 3, 6, 7, 8}.

# list() converte o conjunto em lista; a ordem dos elementos pode variar.
lista_frutas = list(frutas)
print(lista_frutas)