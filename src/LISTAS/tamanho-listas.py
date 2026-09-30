## ====================================== TAMANHO DAS LISTAS ======================================

## VARIAVEIS DE ARRAYS

numeros = [1, 2, 3, 4, 5, 6]
variaveis = [1, "2", "Maria", 4, '5', 6, True, False, 3.14, [ True, False, 3.14 ]]

tNumeros = len(numeros)
tVariaveis = len(variaveis)

## SAIDA DE DADOS

print(tNumeros)
print(tVariaveis)

print(tNumeros -1)
print(tVariaveis -1)

print(numeros)
print(variaveis)

print(f"variaveis[3]: {variaveis[3]}, {type(numeros[3])}") ## SAIDA DE DADOS COM FORMATAÇÃO

## WHILE

while i < tNumeros:
    print(tNumeros[i])
    i += 1