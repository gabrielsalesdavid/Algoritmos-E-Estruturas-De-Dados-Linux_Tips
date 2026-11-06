# ====================================== QUICK SORT ======================================

def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivo = lista[0]
        menores = [x for x in lista[1:] if x <= pivo]
        maiores = [x for x in lista[1:] if x > pivo]
        return quick_sort(menores) + [pivo] + quick_sort(maiores)

lista = [0, 10, 8, 2, 4, 6, 1, 3, 5, 7, 9]
print(quick_sort(lista))

# ====================================== QUICK SORT RANDOM ======================================

import random

lista = [0, 10, 8, 2, 4, 6, 1, 3, 5, 7, 9]

def particionar_aleatorio(lista, inicio, fim):
    indice_sorteado = random.randint(inicio, fim)

    lista[indice_sorteado], lista[fim] = lista[fim], lista[indice_sorteado]

    pivo = lista[fim]
    i = inicio - 1

    for j in range(inicio, fim):
        if lista[j] <= pivo:
            i += 1
            lista[i], lista[j] = lista[j], lista[i]

    lista[i + 1], lista[fim] = lista[fim], lista[i + 1]

    return i + 1

def quick_sort(lista, inicio = 0, fim = None):
    if fim is None:
        fim = len(lista) - 1

    if inicio < fim:
        idx_pivo = particionar_aleatorio(lista, inicio, fim)
        quick_sort(lista, inicio, idx_pivo - 1)
        quick_sort(lista, idx_pivo + 1, fim)

    return lista

print(quick_sort(lista))

# ====================================== QUICK SORT Check ======================================

from abc import ABC, abstractmethod
from collections import Counter


class Ordenador(ABC):
    """Base com validação de entrada e checagens do resultado."""

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


class QuickSort(Ordenador):
    """Quick Sort recursivo (não in-place), com pivô no primeiro elemento."""

    def ordenar(self):
        self._lista = self._quick_sort(self._lista)
        return self.lista

    @classmethod
    def _quick_sort(cls, lista):
        if len(lista) <= 1:
            return lista
        pivo = lista[0]
        menores = [x for x in lista[1:] if x <= pivo]
        maiores = [x for x in lista[1:] if x > pivo]
        return cls._quick_sort(menores) + [pivo] + cls._quick_sort(maiores)


if __name__ == "__main__":
    numeros = [0, 10, 8, 2, 4, 6, 1, 3, 5, 7, 9]

    sorter = QuickSort(numeros)
    print("Antes: ", sorter.lista)
    print("Checagem antes:", sorter.checar())

    sorter.ordenar()
    print("Depois:", sorter.lista)
    print("Checagem depois:", sorter.checar())

    for entrada in ([], "abc", [1, "a", 3]):
        try:
            QuickSort(entrada)
        except (TypeError, ValueError) as e:
            print(f"Erro com {entrada!r}: {e}")

# ====================================== QUICK SORT Pivo ======================================

    @classmethod
    def _quick_sort(cls, lista):
        if len(lista) <= 1:
            return lista
        pivo = lista[len(lista) // 2]
        menores = [x for x in lista if x < pivo]
        iguais  = [x for x in lista if x == pivo]
        maiores = [x for x in lista if x > pivo]
        return cls._quick_sort(menores) + iguais + cls._quick_sort(maiores)

# ====================================== QUICK SORT Contador Global ======================================

contador = {"comparacoes": 0, "chamadas": 0}

def quick_sort(lista):
    contador["chamadas"] += 1

    if len(lista) <= 1:
        return lista

    pivo = lista[0]
    menores = []
    maiores = []

    for x in lista[1:]:
        contador["comparacoes"] += 1
        if x <= pivo:
            menores.append(x)
        else:
            maiores.append(x)

    return quick_sort(menores) + [pivo] + quick_sort(maiores)


lista = [0, 10, 8, 2, 4, 6, 1, 3, 5, 7, 9]
print(quick_sort(lista))
print(f"Comparações: {contador['comparacoes']}")
print(f"Chamadas recursivas: {contador['chamadas']}")

# ====================================== QUICK SORT Contador de Troca ======================================

def quick_sort_inplace(lista, inicio=0, fim=None, contador=None):
    if fim is None:
        fim = len(lista) - 1
    if contador is None:
        contador = {"trocas": 0, "comparacoes": 0}

    if inicio < fim:
        pivo = lista[fim]
        i = inicio - 1

        for j in range(inicio, fim):
            contador["comparacoes"] += 1
            if lista[j] <= pivo:
                i += 1
                lista[i], lista[j] = lista[j], lista[i]
                contador["trocas"] += 1

        lista[i + 1], lista[fim] = lista[fim], lista[i + 1]
        contador["trocas"] += 1

        quick_sort_inplace(lista, inicio, i, contador)
        quick_sort_inplace(lista, i + 2, fim, contador)

    return contador


lista = [0, 10, 8, 2, 4, 6, 1, 3, 5, 7, 9]
resultado = quick_sort_inplace(lista)
print(lista)
print(resultado)