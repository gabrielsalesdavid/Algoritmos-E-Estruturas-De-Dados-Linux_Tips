# ====================================== LISTAS DUPLAMENTE LIGADAS ======================================

# Cada nó mantém referências tanto para o próximo quanto para o anterior.
class NovoDuploNodo:
    def __init__(self, dado):
        self.dados = dado
        self.proximo = None
        self.anterior = None

# A lista guarda referências para as duas extremidades.
class ListaDuplamenteLigada:
    def __init__(self):
        self.cabeca = None
        self.cauda = None

    # Cria um nó e o conecta ao final, atualizando cabeça/cauda quando necessário.
    def inserir(self, dado):
        novo_nodo = NovoDuploNodo(dado)
        # Se não há cabeça, a lista está vazia e o novo nó ocupa as duas pontas.
        if not self.cabeca:
            self.cabeca = novo_nodo
            self.cauda = novo_nodo
            return
        self.cauda.proximo = novo_nodo
        novo_nodo.anterior = self.cauda
        self.cauda = novo_nodo

    # Percorre os nós do início ao fim e informa se encontrou o dado.
    def buscar(self, dado):
        atual = self.cabeca
        while atual:
            if atual.dados == dado:
                return True
            atual = atual.proximo
        return False

    # Remove o nó encontrado, religando os vizinhos e atualizando as extremidades.
    def remover(self, dado):
        if not self.cabeca:
            return
        # Caso especial: a cabeça é o elemento que será removido.
        if self.cabeca.dados == dado:
            self.cabeca = self.cabeca.proximo
            if self.cabeca:
                self.cabeca.anterior = None
            else:
                self.cauda = None
            return
        atual = self.cabeca
        # Avança enquanto houver nó atual e seu dado não for o procurado.
        while atual and atual.dados != dado:
            atual = atual.proximo
        # if atual só executa se a busca encontrou o nó.
        if atual:
            if atual.proximo:
                atual.proximo.anterior = atual.anterior
            else:
                self.cauda = atual.anterior
            if atual.anterior:
                atual.anterior.proximo = atual.proximo

    # Exibe cada dado e avança pela referência proximo até None.
    def imprimir(self):
        atual = self.cabeca
        while atual:
            print(atual.dados, end=" <-> ")
            atual = atual.proximo
        print("None")