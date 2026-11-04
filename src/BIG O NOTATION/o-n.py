# ====================================== O de N ======================================

def busca_linear(lista, alvo):
    for i in range(len(lista)):
        if lista[i] == alvo:
            return i
    return None

linguagens = ["GO", "Java", "JavaScript", "Python"]
print(busca_linear(linguagens, "Python"))