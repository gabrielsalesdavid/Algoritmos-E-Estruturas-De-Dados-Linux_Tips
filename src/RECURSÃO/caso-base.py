# ====================================== CASO BASE ======================================

def abrir_boneca(tamanho):

    if tamanho == 1:
        print("Boneca aberta!")
        return
    else:
        print(f"Boneca de tamanho {tamanho} não pode ser aberta diretamente. Abra a boneca de tamanho {tamanho - 1} primeiro.")
        abrir_boneca(tamanho - 1)

# Saída: Boneca de tamanho 5 não pode ser aberta diretamente. Abra a boneca de tamanho 4 primeiro.
# Boneca de tamanho 4 não pode ser aberta diretamente. Abra a boneca de tamanho 3 primeiro. Boneca de tamanho 3 não pode ser aberta diretamente.
# Abra a boneca de tamanho 2 primeiro. Boneca de tamanho 2 não pode ser aberta diretamente. Abra a boneca de tamanho 1 primeiro. Boneca aberta!
abrir_boneca(5)