# ====================================== BUBBLE SORT ======================================

lista = [0, 5, 3, 8, 6, 2, 1, 4, 7]

def bubble_sort(lista):
    n = len(lista)
    for i in range(n - 1):
        trocou = False
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocou = True
        if not trocou:
            break
    return lista

print(bubble_sort(lista))

# ====================================== BUBBLE SORT - CLASSES ======================================

class Validador:
    @staticmethod
    def esta_ordenada(lista, decrescente=False):
        pares = zip(lista, lista[1:])
        if decrescente:
            return all(a >= b for a, b in pares)
        return all(a <= b for a, b in pares)


class BubbleSort:
    def __init__(self, lista):
        self._lista = list(lista)

    def ordenar(self):
        n = len(self._lista)
        for i in range(n - 1):
            trocou = False
            for j in range(n - i - 1):
                if self._lista[j] > self._lista[j + 1]:
                    self._lista[j], self._lista[j + 1] = self._lista[j + 1], self._lista[j]
                    trocou = True
            if not trocou:
                break
        return self._lista


numeros = [0, 5, 3, 8, 6, 2, 1, 4, 7]
sorter = BubbleSort(numeros)

print(Validador.esta_ordenada(numeros))           # False
print(Validador.esta_ordenada(sorter.ordenar()))  # True

# ===================================== BUBBLE SORT - CLASSES - REFACTOR ======================================

class Ordenador:
    """Responsável por ordenar listas usando Bubble Sort."""

    def __init__(self, lista):
        # Copia a lista para não alterar a original
        self._lista = list(lista)

    @property
    def lista(self):
        return self._lista

    def ordenar(self):
        n = len(self._lista)
        for i in range(n - 1):
            trocou = False
            for j in range(n - i - 1):
                if self._lista[j] > self._lista[j + 1]:
                    self._lista[j], self._lista[j + 1] = self._lista[j + 1], self._lista[j]
                    trocou = True
            if not trocou:
                break
        return self._lista

    def esta_ordenada(self, decrescente=False):
        """Verifica se a lista atual está ordenada (crescente por padrão)."""
        if decrescente:
            return all(self._lista[i] >= self._lista[i + 1]
                    for i in range(len(self._lista) - 1))
        return all(self._lista[i] <= self._lista[i + 1]
                for i in range(len(self._lista) - 1))


if __name__ == "__main__":
    numeros = [0, 5, 3, 8, 6, 2, 1, 4, 7]

    ordenador = Ordenador(numeros)
    print("Antes:", ordenador.lista)
    print("Está ordenada?", ordenador.esta_ordenada())   # False

    ordenador.ordenar()
    print("Depois:", ordenador.lista)
    print("Está ordenada?", ordenador.esta_ordenada())   # True