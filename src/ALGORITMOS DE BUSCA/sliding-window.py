# ====================================== SLIDING WINDOW ======================================

def encontrar_soma_maxima(lista, k):
    if k > len(lista) or k <= 0:
        return 0

    soma_atual = sum(lista[:k])
    soma_maxima = soma_atual

    for i in range(k, len(lista)):
        soma_atual = soma_atual + lista[i] - lista[i - k]

        if soma_atual > soma_maxima:
            soma_maxima = soma_atual

lista = [2, 1, 5, 1, 3, 2]
print(encontrar_soma_maxima(lista, 3))