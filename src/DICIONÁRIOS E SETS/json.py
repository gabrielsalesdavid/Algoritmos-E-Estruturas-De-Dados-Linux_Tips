# ====================================== JSON ======================================

import json  # import disponibiliza o módulo JSON da biblioteca padrão.

# open() retorna um objeto de arquivo; 'r' indica leitura e encoding define a codificação.
arquivo = open('src\DICIONÁRIOS E SETS\brasileirao.json', 'r', encoding='utf-8')

# json.load() interpreta o conteúdo do arquivo e retorna objetos Python (como lista/dict).
dados = json.load(arquivo)

print(dados)  # Exibe os dados carregados.


# for percorre cada registro; o bloco indentado roda uma vez por elemento.
for time_sp in dados:
    # Colchetes acessam o valor de uma chave; == compara valores.
    if time_sp['cidade'] == 'São Paulo':
        print(time_sp)

# Um segundo laço filtra os registros cuja cidade é Rio de Janeiro.
for time_rj in dados:
    if time_rj['cidade'] == 'Rio de Janeiro':
        print(time_rj)

# Procura o registro do Palmeiras e altera seus dados quando encontra o nome.
for titulo in dados:
    if titulo['nome'] == 'Palmeiras':
        # pop() remove/devolve a chave; append() modifica a lista, mas retorna None.
        # Portanto, esta atribuição deixa titulo['titulos'] com valor None.
        titulo['titulos'] = titulo.pop('titulos_brasileiros', []).append('Copa do Brasil 2023')
        print(titulo)

# close() fecha o objeto de arquivo; dados é o conteúdo carregado, não o arquivo.
dados.close()

# Abre o caminho em modo 'w', que cria ou sobrescreve o arquivo.

insercao = open('src\DICIONÁRIOS E SETS\brasileirao.json', 'w', encoding='utf-8')
# dump() serializa o objeto; argumentos nomeados configuram acentos e indentação.
json.dump(dados, insercao, ensure_ascii=False, indent=4)
insercao.close()  # Fecha o objeto de arquivo aberto para escrita.