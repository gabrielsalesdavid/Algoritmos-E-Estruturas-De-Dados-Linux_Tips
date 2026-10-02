## ====================================== OPERAçÕES COM LISTAS ======================================

import sys

sys.stdout.reconfigure(encoding='utf-8') # Permite a exibição de caracteres especiais no terminal

numeros = [1, 2, 3, 4, 5]

pares = [num for num in numeros if num % 2 == 0]
print(pares)

impares = [num for num in numeros if num % 2 != 0]
print(impares)

for num in numeros:
        print(f"{num} é par" if num % 2 == 0 else f"{num} é ímpar")

for num in range(len(numeros)):
    print(f"{num} é par" if numeros[num] % 2 == 0 else f"{num} é ímpar")

mega = [10, 20, 30, 40, 50]
fe = [22, 33, 44, 55, 66]

contador = 0

for num_mega in mega:
    for num_fe in fe:
         if num_mega == num_fe:
             print(f"{num_mega} está em ambas as listas")
             contador += 1

print(f"Total de elementos em comum: {contador}")