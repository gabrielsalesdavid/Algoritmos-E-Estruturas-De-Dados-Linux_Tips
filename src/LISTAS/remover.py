## ====================================== REMOVER ======================================

pokemons = ["Pikachu", "Charmander", "Bulbasaur", "Squirtle", "Jigglypuff", "Pikachu"]

del(pokemons[2])  # Remove "Bulbasaur" from the list
print(pokemons)  # Output: ['Pikachu', 'Charmander', 'Squirtle', 'Jigglypuff']

pokemons.pop(1)  # Remove the element at index 1 from the list
print(pokemons)  # Output: ['Pikachu', 'Squirtle', 'Jigglypuff']

pokemons.remove("Squirtle")  # Remove the element with the value "Squirtle" from the list
print(pokemons)  # Output: ['Pikachu', 'Jigglypuff']

while "Pikachu" in pokemons:
    pokemons.remove("Pikachu")  # Remove all occurrences of "Pikachu" from the list
print(pokemons)  # Output: ['Jigglypuff']