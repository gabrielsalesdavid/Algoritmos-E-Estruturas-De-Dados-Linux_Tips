# ====================================== PILHAS ======================================

# `from ... import ...` importa apenas deque da biblioteca padrão collections.
from collections import deque

# `class` define um novo tipo de objeto; cada instância representa uma pilha.
class Pilha:
    def __init__(self):
        # `__init__` é chamado ao criar uma instância; `self` referencia essa instância.
        self.items = deque()

    def push(self, item):
        # `def` declara um método; o item recebido é colocado no topo da pilha.
        self.items.append(item)

    def pop(self):
        # `not` inverte a condição; `if` executa o bloco indentado se ela for verdadeira.
        if not self.is_empty():
            return self.items.pop()
        else:
            # `raise` interrompe a operação e informa que não há item para remover.
            raise IndexError("pop from an empty stack")

    def peek(self):
        if not self.is_empty():
            # O índice `-1` acessa o último item; `return` o devolve sem removê-lo.
            return self.items[-1]
        else:
            # else cobre o caso em que a condição do if é falsa.
            raise IndexError("peek from an empty stack")

    def is_empty(self):
        # Verifica se a pilha está vazia; `==` produz um resultado booleano.
        return len(self.items) == 0

    def size(self):
        # `len()` retorna a quantidade de elementos armazenados.
        return len(self.items)

    def append(self, item):
        # append() é chamado por meio do ponto e recebe item como argumento.
        self.items.append(item)