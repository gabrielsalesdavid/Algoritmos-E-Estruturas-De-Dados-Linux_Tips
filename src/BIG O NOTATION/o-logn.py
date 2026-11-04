# ====================================== O Log de N ======================================

def busca_binaria(lista, alvo):
    esquerda = 0
    direita = len(lista) - 1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        chute = lista[meio]

        if chute == alvo:
            return meio
        if chute > alvo:
            direita = meio - 1
        else:
            esquerda = meio + 1

    return None

linguagens = ["GO", "Java", "JavaScript", "Python"]
print(busca_binaria(linguagens, "Python"))