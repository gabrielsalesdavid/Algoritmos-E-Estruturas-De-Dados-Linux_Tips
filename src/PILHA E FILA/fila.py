# ====================================== FILA ======================================

from collections import deque

class Fila:
    def __init__(self):
        self._itens = deque()

    def enqueue(self, item):
        self._itens.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Fila vazia")

        return self._itens.popleft()

    def peek(self):
        if self.is_empty():
            return None

        return self._itens[0]

    def is_empty(self):
        return len(self._itens) == 0

    def size(self):
        return len(self._itens)

    def __str__(self):
        if self.is_empty():
            return "Fila vazia"

        return "[Frente] " + " -> ".join(str(item) for item in self._itens) + " -> [Fim]"


nova_fila = Fila()
nova_fila.enqueue(1)
nova_fila.enqueue(2)
print(nova_fila)  # Saída: [Frente] 1 -> 2 -> [Fim]

nova_fila.dequeue()
print(nova_fila)  # Saída: [Frente] 2 -> [Fim]

nova_fila.peek()  # Saída: 2

nova_fila.is_empty()  # Saída: False
