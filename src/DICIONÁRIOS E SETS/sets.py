## ====================================== SETS ======================================

frutas = {"maçã", "banana", "laranja", "uva"} # Cria um conjunto de frutas
print(frutas)

frutas = set() # set() é um método que cria um conjunto vazio
print(frutas)

frutas.add("pera") # Adiciona um elemento ao conjunto
print(frutas)

union = frutas.union({"abacaxi", "manga"}) # Cria um novo conjunto com a união de dois conjuntos
print(union)

sorted_frutas = sorted(frutas) # Ordena o conjunto em ordem alfabética
print(sorted_frutas)

ordered_ascending = sorted(frutas, reverse=True) # Ordena o conjunto em ordem decrescente
ordered_descending = sorted(frutas, reverse=False) # Ordena o conjunto em ordem crescente
print(ordered_ascending)
print(ordered_descending)

# Intersection: Retorna um novo conjunto com os elementos que estão presentes em ambos os conjuntos
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {4, 5, 6, 7, 8}
intersecao = conjunto1.intersection(conjunto2)
print(intersecao) # Saída: {4, 5}

# Difference: Retorna um novo conjunto com os elementos que estão presentes no primeiro conjunto, mas não no segundo
diferenca = conjunto1.difference(conjunto2)
print(diferenca) # Saída: {1, 2, 3}

# Symmetric Difference: Retorna um novo conjunto com os elementos que estão presentes em um dos conjuntos, mas não em ambos
diferenca_simetrica = conjunto1.symmetric_difference(conjunto2)
print(diferenca_simetrica) # Saída: {1, 2, 3, 6, 7, 8}

# list: Converte o conjunto em uma lista
lista_frutas = list(frutas)
print(lista_frutas) # Saída: ['banana', 'laranja', 'maçã', 'pera', 'uva']