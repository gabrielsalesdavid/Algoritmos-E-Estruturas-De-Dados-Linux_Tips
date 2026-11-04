# ====================================== O N ao Quadrado ======================================

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

linguagens = ["Python", "GO", "Java", "JavaScript"]
print(bubble_sort(linguagens))