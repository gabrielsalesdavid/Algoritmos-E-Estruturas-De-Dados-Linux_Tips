# ====================================== LAÇO FOR ======================================

# Uma lista literal guarda as cores a serem percorridas pelo for.
cores = ['verde', 'amarelo', 'azul', 'branco']

# A sintaxe for variavel in iteravel atribui cada item à variável cor.
for cor in cores:
    print(cor)

# range(inicio, limite) inclui inicio e exclui limite.
for numero in range(1, 11):
    print(numero)

# O terceiro argumento de range() define o passo entre os valores.
for numero in range(1, 11, 2):
    print(numero)