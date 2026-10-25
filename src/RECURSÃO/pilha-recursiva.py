# ====================================== PILHA RECURSIVA ======================================

map_categoria = {
    1: {"nome": "Eletrônicos", "subcategorias": {1: "Celulares", 2: "Computadores"}},
    2: {"nome": "Roupas", "subcategorias": {1: "Masculino", 2: "Feminino"}},
    3: {"nome": "Alimentos", "subcategorias": {1: "Frescos", 2: "Congelados"}}
}

def gerar_trilha_breadcrumbs(categoria_id, subcategoria_id):
    if categoria_id in map_categoria:
        categoria = map_categoria[categoria_id]
        nome_categoria = categoria["nome"]
        subcategorias = categoria["subcategorias"]

        if subcategoria_id in subcategorias:
            nome_subcategoria = subcategorias[subcategoria_id]
            return f"{nome_categoria} > {nome_subcategoria}"
        else:
            return f"{nome_categoria} > Subcategoria não encontrada"
    else:
        return "Categoria não encontrada"

if __name__ == "__main__":
    print("Categorias disponíveis:")
    for categoria_id, categoria_info in map_categoria.items():
        print(f"{categoria_id}: {categoria_info['nome']}")

    categoria_id = int(input("Digite o ID da categoria: "))
    subcategoria_id = int(input("Digite o ID da subcategoria: "))

    trilha_breadcrumbs = gerar_trilha_breadcrumbs(categoria_id, subcategoria_id)
    print(f"Trilha de breadcrumbs: {trilha_breadcrumbs}")