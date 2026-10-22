# ====================================== OPERAÇÕES COM LISTAS ======================================

import sys  # import carrega o módulo para acessar recursos do interpretador.

# stdout representa a saída padrão; a chamada configura sua codificação.
sys.stdout.reconfigure(encoding='utf-8')

# Listas guardam itens em uma sequência indexada.
numeros = [1, 2, 3, 4, 5]

# Compreensão de lista: expressão, laço e filtro produzem uma lista nova.
# % calcula o resto da divisão; == 0 seleciona os números pares.
pares = [num for num in numeros if num % 2 == 0]
print(pares)

# != significa "diferente"; este filtro seleciona valores ímpares.
impares = [num for num in numeros if num % 2 != 0]
print(impares)

# for atribui cada elemento à variável num; a expressão condicional escolhe
# entre os textos antes de print() exibi-los.
for num in numeros:
        print(f"{num} é par" if num % 2 == 0 else f"{num} é ímpar")

# range() gera índices; len() fornece a quantidade usada como limite do laço.
for num in range(len(numeros)):
    # numeros[num] acessa o elemento no índice; f-string inclui o valor calculado.
    print(f"{num} é par" if numeros[num] % 2 == 0 else f"{num} é ímpar")

# Duas listas independentes usadas para comparar elementos.
mega = [10, 20, 30, 40, 50]
fe = [22, 33, 44, 55, 66]

contador = 0

# Laços for aninhados testam cada combinação de valores das duas listas.
for num_mega in mega:
    for num_fe in fe:
         # if executa quando os valores são iguais; += incrementa o contador.
         if num_mega == num_fe:
             print(f"{num_mega} está em ambas as listas")
             contador += 1

# A variável contador é interpolada para mostrar o total encontrado.
print(f"Total de elementos em comum: {contador}")