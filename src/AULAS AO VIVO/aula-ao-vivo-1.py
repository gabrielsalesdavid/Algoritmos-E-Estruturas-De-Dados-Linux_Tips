# ====================================== LiSTAS ======================================

def pegar_primeiro_item(lista):

    retorno = lista[0]

    for maior in lista:
        if maior > retorno:
            retorno = maior

    return retorno

linguagens = ["Python", "GO", "Java", "JavaScript"]
print(pegar_primeiro_item(linguagens))

numero_maiores = [2, 4, 16, 24, 36, 48, 78, 98]
print(pegar_primeiro_item(numero_maiores))