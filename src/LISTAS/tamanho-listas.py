## ====================================== TAMANHO DAS LISTAS ======================================

## VARIAVEIS DE ARRAYS

numeros = [1, 2, 3, 4, 5, 6]
variaveis = [1, "2", "Maria", 4, '5', 6, True, False, 3.14, [ True, False, 3.14 ]]

t_numeros = len(numeros)
t_variaveis = len(variaveis)

## SAIDA DE DADOS

print(t_numeros)
print(t_variaveis)

print(t_numeros -1)
print(t_variaveis -1)

print(numeros)
print(variaveis)

print(f"variaveis[3]: {variaveis[3]}, {type(numeros[3])}") ## SAIDA DE DADOS COM FORMATAÇÃO

## WHILE

while i < t_numeros:
    print(t_numeros[i])
    i += 1