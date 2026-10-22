# ====================================== DICIONÁRIOS E LISTAS ======================================

# Colchetes criam uma lista; cada elemento abaixo é um dicionário.
times = [
    {"nome": "Time A", "cidade": "São Paulo"},
    {"nome": "Time B", "cidade": "Rio de Janeiro"},
    {"nome": "Time C", "cidade": "Brasília"},
    {"nome": "Time D", "cidade": "Salvador"}
]

# for percorre a lista e atribui cada elemento temporariamente a time.
for time in times:
    # A condição compara o valor da chave cidade com a string indicada.
    if time["cidade"] == "São Paulo":
        # f-string interpola expressões entre {}; colchetes acessam as chaves do dict.
        print(f"Nome: {time['nome']}, Cidade: {time['cidade']}")