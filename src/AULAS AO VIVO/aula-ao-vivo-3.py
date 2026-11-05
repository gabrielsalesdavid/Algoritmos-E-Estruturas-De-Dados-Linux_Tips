# ====================================== NÓ ======================================

class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

def tamanho(elementos):
    cabeca = None
    atual = None

    for item in elementos:
        novo_no = No(item)
        if cabeca is None:
            cabeca = novo_no
            atual = cabeca
        else:
            atual.proximo = novo_no
            atual = atual.proximo

    # Calcular o tamanho da lista
    contador = 0
    atual = cabeca
    while atual is not None:
        contador += 1
        atual = atual.proximo

    return contador