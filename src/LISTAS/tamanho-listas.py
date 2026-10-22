# ====================================== TAMANHO DAS LISTAS ======================================

# Uma lista é criada com colchetes; pode reunir valores de tipos diferentes.

numeros = [1, 2, 3, 4, 5, 6]
variaveis = [1, "2", "Maria", 4, '5', 6, True, False, 3.14, [ True, False, 3.14 ]]

# len() devolve a quantidade de elementos; o resultado é guardado com =.
t_numeros = len(numeros)
t_variaveis = len(variaveis)

# print() exibe cada argumento no terminal.

print(t_numeros)
print(t_variaveis)

# - realiza subtração; o último índice de uma lista é seu tamanho menos um.
print(t_numeros -1)
print(t_variaveis -1)

print(numeros)
print(variaveis)

# f-string interpola expressões entre chaves; índices de listas começam em zero.
print(f"variaveis[3]: {variaveis[3]}, {type(numeros[3])}")

# while repete o bloco enquanto a condição for verdadeira.
# Neste exemplo, i precisa ser inicializada antes do laço; além disso,
# t_numeros é um inteiro e não pode ser indexado como t_numeros[i].

while i < t_numeros:
    print(t_numeros[i])
    # += soma 1 ao valor atual e o reatribui à variável.
    i += 1