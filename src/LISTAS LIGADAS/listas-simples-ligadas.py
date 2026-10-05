## ====================================== LISTAS SIMPLES LIGADAS ======================================

class Nodo:
    def __init__(self, dado):
        self.dados = dado
        self.proximo = None

# Criação da lista simplesmente ligada
class ListaSimplesLigada:
    def __init__(self):
        self.cabeca = None

# Inserção de um novo nó no final da lista
    def inserir(self, dado):
        novo_nodo = Nodo(dado)
        if not self.cabeca:
            self.cabeca = novo_nodo
            return
        atual = self.cabeca
        while atual.proximo:
            atual = atual.proximo
        atual.proximo = novo_nodo

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
            return
        atual = self.cabeca
        while atual.proximo and atual.proximo.dados != dado:
            atual = atual.proximo
        if atual.proximo:
            atual.proximo = atual.proximo.proximo

# Impressão da lista ligada
    def imprimir(self):
        atual = self.cabeca
        while atual:
            print(atual.dados, end=" -> ")
            atual = atual.proximo
        print("None")