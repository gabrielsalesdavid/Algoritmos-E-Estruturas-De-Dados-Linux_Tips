# ====================================== TABELA HASH ======================================

print("--- 1. O Dicionário como Tabela Hash ---")

catalogo_produtos = {
    "SKU101": {"nome": "Teclado Mecânico", "preco": 350.00, "estoque": 45},
    "SKU202": {"nome": "Mouse Sem Fio", "preco": 120.00, "estoque": 12},
    "SKU303": {"nome": "Monitor 27", "preco": 1400.00, "estoque": 5},
}

produto_buscado = "SKU202"

resultado = catalogo_produtos.get(produto_buscado)

if resultado:
    print(f"Produto Encontrado Instantaneamente: {resultado['nome']} - R$ {resultado['preco']}")
else:
    print("Produto não localizado.")

catalogo_produtos["SKU404"] = {"nome": "Cadeira Gamer", "preco": 1200.00, "estoque": 2}
print("\nCatálogo atualizado com a cadeira!")

removido = catalogo_produtos.pop("SKU101")
print(f"Produto {removido['nome']} removido do sistema.")