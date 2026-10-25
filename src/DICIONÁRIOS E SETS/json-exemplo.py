# ====================================== EXEMPLO JSON ======================================

import json  # import disponibiliza o módulo JSON da biblioteca padrão.
from pathlib import Path

# Path(__file__) localiza este script; with fecha o arquivo ao sair do bloco.
caminho_arquivo = Path(__file__).with_name("brasileirao.json")
with caminho_arquivo.open("r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

print(dados)  # Exibe os dados carregados.


# for percorre cada registro; o bloco indentado roda uma vez por elemento.
for time_sp in dados:
    # Colchetes acessam o valor de uma chave; == compara valores.
    if time_sp['endereco']['cidade'] == 'São Paulo':
        print(time_sp)

# Um segundo laço filtra os registros cuja cidade é Rio de Janeiro.
for time_rj in dados:
    if time_rj['endereco']['cidade'] == 'Rio de Janeiro':
        print(time_rj)

# Procura o registro do Palmeiras e altera seus dados quando encontra o nome.
for titulo in dados:
    if titulo['nome'] == 'Palmeiras':
        # pop() recupera a lista antiga; a alternativa permite executar o exemplo novamente.
        titulos = titulo.pop('titulos_brasileiros', titulo.get('titulos', []))
        if 'Copa do Brasil 2023' not in titulos:
            titulos.append('Copa do Brasil 2023')
        titulo['titulos'] = titulos
        print(titulo)

# Abre o arquivo em modo 'w', que cria ou sobrescreve o conteúdo existente.
with caminho_arquivo.open("w", encoding="utf-8") as insercao:
    # dump() serializa o objeto; argumentos nomeados configuram acentos e indentação.
    json.dump(dados, insercao, ensure_ascii=False, indent=4)