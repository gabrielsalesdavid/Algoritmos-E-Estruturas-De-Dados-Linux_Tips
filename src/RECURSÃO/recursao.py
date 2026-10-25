# ====================================== RECURSAO ======================================

def contagem_regressiva(n):
    if n <= 0:
        print("BUMMMMMM!!!!")
    else:
        print(n)
        contagem_regressiva(n - 1)

contagem_regressiva(5)  # Saída: 5, 4, 3, 2, 1, BUMMMMMM!!!!