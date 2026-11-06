# ====================================== BUSCA BINARIA ======================================

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def busca_binaria_classica(lista, alvo):
    inicio = 0
    fim = len(lista) -1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if lista[meio] == alvo:
            return meio

        elif lista[meio] > alvo:
            fim = meio - 1
        else:
            inicio = meio + 1

    return -1

print(busca_binaria_classica(lista, 5))