## ====================================== MATRIZES ======================================

linha = [1, 2, 3, 4, 5]

tabuleiro = [
    ['X', 'O', 'X'],
    ['O', 'X', 'O'],
    ['X', 'O', 'X']
]

print(tabuleiro[0][0])

# Matriz 3x3 representando as cadeiras de um cinema
cinema = [
   [19, 20, 3],
   [48, 5, 22],
   [7, 18, 33]
]

soma_maiores = 0

print("Iniciando varredura da sala de cinema...")

# 1. O laço externo controla a LINHA
for linha in range(len(cinema)):
    
    # 2. O laço interno controla a COLUNA da linha atual 'linha'
    for coluna in range(len(cinema[linha])):
        
        # Guardamos a idade da cadeira atual em uma variável para ficar fácil de ler
        idade_atual = cinema[linha][coluna]
        
        # 3. Operação complexa dentro do laço aninhado
        if idade_atual >= 18:
            print("Adulto encontrado na Linha " + str(linha) + ", Coluna " + str(coluna) + " - Idade: " + str(idade_atual))
            soma_maiores += idade_atual

print("\nA soma das idades dos adultos é: " + str(soma_maiores))