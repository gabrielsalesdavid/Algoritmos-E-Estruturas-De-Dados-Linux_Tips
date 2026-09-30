## ====================================== ADICIONAR ELEMENTOS ======================================

sacola = ["maçã", "banana", "laranja"]

## append() - ADICIONAR

sacola.append("uva")  # Adiciona "uva" no final da lista

## SAIDA DE DADOS

print(sacola)  # Saída: ['maçã', 'banana', 'laranja', 'uva']

## push() - ADICIONAR (não existe em Python, mas é equivalente ao append())

sacola.push("abacaxi")  # Adiciona "abacaxi" no final da lista (equivalente ao append())

## insert() - ADICIONAR EM UMA POSIÇÃO ESPECÍFICA

sacola.insert(1, "pera")  # Adiciona "pera" na posição 1 da lista

## extend() - ADICIONAR VÁRIOS ELEMENTOS

sacola.extend(["kiwi", "manga"])  # Adiciona "kiwi" e "manga" no final da lista