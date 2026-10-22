# ====================================== LISTAS ======================================

# Listas usam colchetes; os elementos podem ter tipos diferentes.

numeros = [1, 2, 3, 4, 5, 6]
variaveis = [1, "2", "Maria", 4, '5', 6, True, False, 3.14, [ True, False, 3.14 ]]

# Índices começam em zero; colchetes acessam o elemento naquela posição.

print(numeros[3])
print(variaveis[3])
# f-string permite inserir expressões entre chaves; type() retorna o tipo do valor.
print(f"variaveis[3]: {variaveis[3]}, {type(numeros[3])}")