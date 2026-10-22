# ====================================== DICIONÁRIOS ======================================

# Chaves e valores de um dicionário são escritos como chave: valor entre chaves.
# Aqui, porém, cada elemento é outro dict sem par chave: valor externo: isso cria
# uma tentativa de conjunto e falha porque dicts não podem ser elementos de set.
pessoa = {
    {"nome": "Alice",
    "idade": 30,
    "cidade": "São Paulo"},
    {"nome": "Bob",
    "idade": 25,
    "cidade": "Rio de Janeiro"}
}

# Colchetes acessam um valor pela chave (esta linha pressupõe que pessoa seja dict).
print(pessoa["nome"])