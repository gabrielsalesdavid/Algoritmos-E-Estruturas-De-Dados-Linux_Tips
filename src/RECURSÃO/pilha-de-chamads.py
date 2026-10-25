# ====================================== PILHA DE CHAMADAS ======================================

def obter_taxa_imposto(estado):
    if estado == "SP":
        return 0.18
    elif estado == "RJ":
        return 0.20
    elif estado == "MG":
        return 0.15
    else:
        return 0.10

def calcular_preco_final(valor_base, uf_destino):
    taxa_imposto = obter_taxa_imposto(uf_destino) # Chamada da função obter_taxa_imposto
    preco_final = valor_base * (1 + taxa_imposto)
    return preco_final

def fechar_carrinho_cliente(nome, preco_produto, uf_cliente):
    preco_final = calcular_preco_final(preco_produto, uf_cliente) # Chamada da função calcular_preco_final
    print(f"Cliente: {nome}")
    print(f"Preço final do produto: R$ {preco_final:.2f}")

if __name__ == "__main__":
    nome_cliente = input("Digite o nome do cliente: ")
    preco_produto = float(input("Digite o preço do produto: "))
    uf_cliente = input("Digite a UF do cliente (SP, RJ, MG ou outro): ")

    fechar_carrinho_cliente(nome_cliente, preco_produto, uf_cliente)