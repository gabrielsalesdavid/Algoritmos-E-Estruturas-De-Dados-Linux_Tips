# ====================================== SELECTION SORT ======================================

lista = [0, 10, 8, 2, 4, 6, 1, 3, 5, 7, 9]

def encontrar_menor(lista):
    menor_valor = lista[0]
    menor_indice = 0
    for i in range(1, len(lista)):
        if lista[i] < menor_valor:
            menor_valor = lista[i]
            menor_indice = i
    return menor_indice

def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        menor_indice = encontrar_menor(lista[i:]) + i
        lista[i], lista[menor_indice] = lista[menor_indice], lista[i]
    return lista

print(selection_sort(lista))

# ====================================== SELECTION SORT POO Validação ======================================

from collections import Counter


class SelectionSort:
    """Ordena uma lista com Selection Sort, validando entrada e resultado."""

    def __init__(self, lista):
        self._validar_entrada(lista)
        self._original = list(lista)   # guarda o estado inicial para a checagem
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
        return list(self._lista)       # devolve cópia, protege o estado interno

    # ---------- Algoritmo ----------
    def _encontrar_menor(self, inicio):
        """Retorna o índice do menor valor a partir de `inicio`."""
        menor_indice = inicio
        for i in range(inicio + 1, len(self._lista)):
            if self._lista[i] < self._lista[menor_indice]:
                menor_indice = i
        return menor_indice

    def ordenar(self):
        n = len(self._lista)
        for i in range(n - 1):
            menor_indice = self._encontrar_menor(i)
            if menor_indice != i:
                self._lista[i], self._lista[menor_indice] = (
                    self._lista[menor_indice], self._lista[i]
                )
        return self.lista

    # ---------- Checagens ----------
    def esta_ordenada(self, decrescente=False):
        """Verifica se cada elemento respeita a ordem em relação ao próximo."""
        pares = zip(self._lista, self._lista[1:])
        if decrescente:
            return all(a >= b for a, b in pares)
        return all(a <= b for a, b in pares)

    def preservou_elementos(self):
        """Confere se o resultado tem exatamente os mesmos elementos da original
        (nada perdido, nada duplicado)."""
        return Counter(self._original) == Counter(self._lista)

    def checar(self):
        """Resumo completo da verificação."""
        return {
            "ordenada": self.esta_ordenada(),
            "mesmos_elementos": self.preservou_elementos(),
            "tamanho_igual": len(self._original) == len(self._lista),
        }


if __name__ == "__main__":
    numeros = [0, 10, 8, 2, 4, 6, 1, 3, 5, 7, 9]

    sorter = SelectionSort(numeros)
    print("Antes: ", sorter.lista)
    print("Checagem antes:", sorter.checar())

    sorter.ordenar()
    print("Depois:", sorter.lista)
    print("Checagem depois:", sorter.checar())

    # Validação de entrada
    for entrada in ([], "abc", [1, "a", 3]):
        try:
            SelectionSort(entrada)
        except (TypeError, ValueError) as e:
            print(f"Erro com {entrada!r}: {e}")