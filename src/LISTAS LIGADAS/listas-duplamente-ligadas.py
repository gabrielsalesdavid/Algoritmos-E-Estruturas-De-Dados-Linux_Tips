## ====================================== LISTAS DUPLEMENTE LIGADAS ======================================
class NovoDuploNodo:
    def __init__(self, dado):
        self.dados = dado
        self.proximo = None
        self.anterior = None

# Criação da lista duplamente ligada
class ListaDuplamenteLigada:
    def __init__(self):
        self.cabeca = None
        self.cauda = None

# Inserção de um novo nó no final da lista
    def inserir(self, dado):
        novo_nodo = NovoDuploNodo(dado)
        if not self.cabeca:
            self.cabeca = novo_nodo
            self.cauda = novo_nodo
            return
        self.cauda.proximo = novo_nodo
        novo_nodo.anterior = self.cauda
        self.cauda = novo_nodo

# Busca de um nó com um valor específico
    def buscar(self, dado):
        atual = self.cabeca
        while atual:
            if atual.dados == dado:
                return True
            atual = atual.proximo
        return False

# Remoção de um nó com um valor específico
    def remover(self, dado):
        if not self.cabeca:
            return
        if self.cabeca.dados == dado:
            self.cabeca = self.cabeca.proximo
            if self.cabeca:
                self.cabeca.anterior = None
            else:
                self.cauda = None
            return
        atual = self.cabeca
        while atual and atual.dados != dado:
            atual = atual.proximo
        if atual:
            if atual.proximo:
                atual.proximo.anterior = atual.anterior
            else:
                self.cauda = atual.anterior
            if atual.anterior:
                atual.anterior.proximo = atual.proximo

# Impressão da lista duplamente ligada
    def imprimir(self):
        atual = self.cabeca
        while atual:
            print(atual.dados, end=" <-> ")
            atual = atual.proximo
        print("None")