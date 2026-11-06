# ====================================== INSERTION SORT ======================================

def insertion_sort(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = chave
    return lista

lista = [0, 10, 8, 2, 4, 6, 1, 3, 5, 7, 9]
print(insertion_sort(lista))

# ====================================== INSERTION SORT POO Validação ======================================

from collections import Counter

class InsertionSort:
    """Ordena uma lista com Insertion Sort, validando entrada e resultado."""

    def __init__(self, lista):
        self._validar_entrada(lista)
        self._original = list(lista)   # estado inicial, usado na checagem
        self._lista = list(lista)      # cópia de trabalho

    # ---------- Validação da entrada ----------
    @staticmethod
    def _validar_entrada(lista):
        if not isinstance(lista, list):
            raise TypeError("A entrada deve ser uma lista.")
        if not lista:
            raise ValueError("A lista não pode ser vazia.")
        if not all(isinstance(x, (int, float)) and not isinstance(x, bool)
                for x in lista):
            raise TypeError("Todos os elementos devem ser números (int ou float).")

    @property
    def lista(self):
        return list(self._lista)

    # ---------- Algoritmo ----------
    def ordenar(self):
        for i in range(1, len(self._lista)):
            chave = self._lista[i]
            j = i - 1
            # desloca para a direita os elementos maiores que a chave
            while j >= 0 and self._lista[j] > chave:
                self._lista[j + 1] = self._lista[j]
                j -= 1
            self._lista[j + 1] = chave
        return self.lista

    # ---------- Checagens ----------
    def esta_ordenada(self, decrescente=False):
        pares = zip(self._lista, self._lista[1:])
        if decrescente:
            return all(a >= b for a, b in pares)
        return all(a <= b for a, b in pares)

    def preservou_elementos(self):
        return Counter(self._original) == Counter(self._lista)

    def checar(self):
        return {
            "ordenada": self.esta_ordenada(),
            "mesmos_elementos": self.preservou_elementos(),
            "tamanho_igual": len(self._original) == len(self._lista),
        }


if __name__ == "__main__":
    numeros = [0, 10, 8, 2, 4, 6, 1, 3, 5, 7, 9]

    sorter = InsertionSort(numeros)
    print("Antes: ", sorter.lista)
    print("Checagem antes:", sorter.checar())

    sorter.ordenar()
    print("Depois:", sorter.lista)
    print("Checagem depois:", sorter.checar())

    for entrada in ([], "abc", [1, "a", 3]):
        try:
            InsertionSort(entrada)
        except (TypeError, ValueError) as e:
            print(f"Erro com {entrada!r}: {e}")

# ====================================== INSERTION SORT Check ======================================

from abc import ABC, abstractmethod
from collections import Counter


class Ordenador(ABC):
    def __init__(self, lista):
        self._validar_entrada(lista)
        self._original = list(lista)
        self._lista = list(lista)

    @staticmethod
    def _validar_entrada(lista):
        if not isinstance(lista, list):
            raise TypeError("A entrada deve ser uma lista.")
        if not lista:
            raise ValueError("A lista não pode ser vazia.")
        if not all(isinstance(x, (int, float)) and not isinstance(x, bool)
                for x in lista):
            raise TypeError("Todos os elementos devem ser números (int ou float).")

    @property
    def lista(self):
        return list(self._lista)

    @abstractmethod
    def ordenar(self):
        """Cada algoritmo implementa o seu."""

    def esta_ordenada(self, decrescente=False):
        pares = zip(self._lista, self._lista[1:])
        return all(a >= b for a, b in pares) if decrescente else all(a <= b for a, b in pares)

    def preservou_elementos(self):
        return Counter(self._original) == Counter(self._lista)

    def checar(self):
        return {
            "ordenada": self.esta_ordenada(),
            "mesmos_elementos": self.preservou_elementos(),
            "tamanho_igual": len(self._original) == len(self._lista),
        }


class InsertionSort(Ordenador):
    def ordenar(self):
        for i in range(1, len(self._lista)):
            chave = self._lista[i]
            j = i - 1
            while j >= 0 and self._lista[j] > chave:
                self._lista[j + 1] = self._lista[j]
                j -= 1
            self._lista[j + 1] = chave
        return self.lista