## ====================================== JSON ======================================

import json # Importa o módulo json para trabalhar com arquivos JSON

arquivo = open('src\DICIONÁRIOS E SETS\brasileirao.json', 'r', encoding='utf-8') # Abre o arquivo JSON em modo de leitura

dados = json.load(arquivo) # Carrega os dados do arquivo JSON para um dicionário Python

print(dados) # Saída: {'nome': 'João', 'idade': 30, 'cidade': 'São Paulo'}


# Os times de São Paulo
for time_sp in dados:
    if time_sp['cidade'] == 'São Paulo':
        print(time_sp)

# Os times do RJ
for time_rj in dados:
    if time_rj['cidade'] == 'Rio de Janeiro':
        print(time_rj)

# Adicionando um novo título ao Palmeiras
for titulo in dados:
    if titulo['nome'] == 'Palmeiras':
        # Renomeia a chave 'titulos_brasileiros' para 'titulos' e adiciona um novo título à lista de títulos do Palmeiras
        titulo['titulos'] = titulo.pop('titulos_brasileiros', []).append('Copa do Brasil 2023') # Alias
        print(titulo)