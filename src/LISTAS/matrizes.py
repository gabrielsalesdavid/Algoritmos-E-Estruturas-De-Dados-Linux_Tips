# ====================================== MATRIZES ======================================

# Uma matriz pode ser representada como lista de listas.
linha = [1, 2, 3, 4, 5]

tabuleiro = [
    ['X', 'O', 'X'],
    ['O', 'X', 'O'],
    ['X', 'O', 'X']
]

# Índices encadeados escolhem primeiro a linha e depois a coluna (base zero).
print(tabuleiro[0][0])

# Matriz 3x3 representando as cadeiras de um cinema
cinema = [
   [19, 20, 3],
   [48, 5, 22],
   [7, 18, 33]
]

soma_maiores = 0

print("Iniciando varredura da sala de cinema...")

# range(n) produz índices de 0 até n-1; o laço externo percorre as linhas.
for linha in range(len(cinema)):
    
    # O laço interno percorre os índices de coluna da linha atual.
    for coluna in range(len(cinema[linha])):
        
        # Acessos com dois índices selecionam o elemento linha/coluna.
        idade_atual = cinema[linha][coluna]
        
        # >= compara se a idade alcança o limite; if controla o bloco indentado.
        if idade_atual >= 18:
            # str() converte números em texto para concatená-los com strings.
            print("Adulto encontrado na Linha " + str(linha) + ", Coluna " + str(coluna) + " - Idade: " + str(idade_atual))
            # += acumula a idade no total anterior.
            soma_maiores += idade_atual

print("\nA soma das idades dos adultos é: " + str(soma_maiores))