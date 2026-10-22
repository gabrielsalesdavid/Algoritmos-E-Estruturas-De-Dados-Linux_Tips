# ====================================== REMOVER ======================================

# Lista literal com strings; valores repetidos são permitidos.
pokemons = ["Pikachu", "Charmander", "Bulbasaur", "Squirtle", "Jigglypuff", "Pikachu"]

# del remove o elemento indicado pelo índice entre colchetes.
del(pokemons[2])
print(pokemons)

# pop(indice) remove e devolve o item naquela posição.
pokemons.pop(1)
print(pokemons)  # Output: ['Pikachu', 'Squirtle', 'Jigglypuff']

# remove(valor) remove a primeira ocorrência do valor informado.
pokemons.remove("Squirtle")
print(pokemons)  # Output: ['Pikachu', 'Jigglypuff']

# in testa pertencimento; while continua enquanto houver "Pikachu" na lista.
while "Pikachu" in pokemons:
    pokemons.remove("Pikachu")  # Cada repetição remove uma ocorrência.
print(pokemons)  # Output: ['Jigglypuff']