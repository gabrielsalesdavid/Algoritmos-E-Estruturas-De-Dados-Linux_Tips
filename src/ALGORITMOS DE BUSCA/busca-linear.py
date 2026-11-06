# ====================================== BUSCA LINEAR ======================================

def busca_linear(lista, elemento_alvo):
    for indice, valor_atual in enumerate(lista):
        if valor_atual == elemento_alvo:
            return valor_atual

    return - 1

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(busca_linear(lista, 8))

# ====================================== BUSCA LINEAR Sentinela ======================================

def busca_linear_sentinela(lista, elemento_alvo):
    lista.append(elemento_alvo)

    indice = 0

    while lista[indice] != elemento_alvo:
        indice += 1

    lista.pop()

    if indice < len(lista):
        return indice
    else:
        return -1

print(busca_linear_sentinela(lista, 9))

# ====================================== BUSCA LINEAR Memoravel ======================================

def criar_busca_memoizada(lista):
    cache = {}

    def busca(elemento_alvo):
        if elemento_alvo in cache:
            return cache[elemento_alvo]          # O(1) se já buscou antes

        for indice, valor_atual in enumerate(lista):
            if valor_atual == elemento_alvo:
                cache[elemento_alvo] = indice
                return indice

        cache[elemento_alvo] = -1
        return -1

    return busca


lista = [0, 5, 3, 8, 6, 2, 1, 4, 7]
busca = criar_busca_memoizada(lista)

print(busca(8))  # 3  (percorre a lista)
print(busca(8))  # 3  (vem direto do cache)
print(busca(9))  # -1 (percorre a lista)
print(busca(9))  # -1 (vem do cache)

# ====================================== BUSCA LINEAR em Cache ======================================

from functools import lru_cache

lista = (0, 5, 3, 8, 6, 2, 1, 4, 7)

@lru_cache(maxsize=None)
def busca_linear(elemento_alvo):
    for indice, valor_atual in enumerate(lista):
        if valor_atual == elemento_alvo:
            return indice
    return -1

print(busca_linear(8))  # 3
print(busca_linear(8))  # cache hit