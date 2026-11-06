# ====================================== DOIS PONTEIROS ======================================

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
alvo = 6

def two_pointers(lista, alvo):
    esq = 0
    dir = len(lista) -1

    while esq < dir:
        soma = lista[esq] + lista[dir]

        if soma == alvo:
            return [lista[esq], lista[dir]]
        elif soma < alvo:
            esq += 1
        else:
            dir -= 1

    return -1

print(two_pointers(lista, alvo))

# ====================================== DUAS SOMAS ======================================

class Solution:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]

        return []

# ====================================== DUAS SOMAS ======================================

class Solution:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        nums_com_indices = [(num, i) for i, num in enumerate(nums)]
        nums_com_indices.sort(key = lambda x: x [0])

        esq = 0
        dir = len(nums) -1

        while esq < dir:
            soma = nums_com_indices[esq][0] + nums_com_indices[dir][0]
            if soma == target:
                return [nums_com_indices[esq][1], nums_com_indices[dir][1]]
            elif soma < target:
                esq += 1
            else:
                dir -= 1

        return []