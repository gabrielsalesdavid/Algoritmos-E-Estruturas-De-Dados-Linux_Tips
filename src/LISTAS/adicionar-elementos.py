# ====================================== ADICIONAR ELEMENTOS ======================================

# Atribuição guarda uma lista de strings na variável sacola.
sacola = ["maçã", "banana", "laranja"]

# append(valor) chama o método da lista para incluir um item ao final.

sacola.append("uva")  # Adiciona "uva" no final da lista

# print() mostra a lista atual.

print(sacola)  # Saída: ['maçã', 'banana', 'laranja', 'uva']

# Listas Python não possuem método push(); esta chamada gera AttributeError.

sacola.push("abacaxi")  # Adiciona "abacaxi" no final da lista (equivalente ao append())

# insert(indice, valor) insere um elemento na posição indicada.

sacola.insert(1, "pera")  # Adiciona "pera" na posição 1 da lista

# extend(iteravel) acrescenta à lista todos os itens do iterável fornecido.

sacola.extend(["kiwi", "manga"])  # Adiciona "kiwi" e "manga" no final da lista