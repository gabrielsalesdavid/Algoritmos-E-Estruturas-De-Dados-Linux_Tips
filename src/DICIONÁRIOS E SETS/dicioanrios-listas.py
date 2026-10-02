## ====================================== DICIONÁRIOS LISTAS ======================================

times = [
    {"nome": "Time A", "cidade": "São Paulo"},
    {"nome": "Time B", "cidade": "Rio de Janeiro"},
    {"nome": "Time C", "cidade": "Brasília"},
    {"nome": "Time D", "cidade": "Salvador"}
]

for time in times:
    if time["cidade"] == "São Paulo":
        print(f"Nome: {time['nome']}, Cidade: {time['cidade']}")