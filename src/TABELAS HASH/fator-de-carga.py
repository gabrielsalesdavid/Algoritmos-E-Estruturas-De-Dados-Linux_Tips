# ====================================== FATOR DE CARGA ======================================

def fator_de_carga(quantidade_itens: int, capacidade: int) -> float:
    """
    Calcula a ocupação de uma tabela hash: quantidade de itens / capacidade.
    """
    if quantidade_itens < 0:
        raise ValueError("A quantidade de itens não pode ser negativa.")
    if capacidade <= 0:
        raise ValueError("A capacidade da tabela deve ser maior que zero.")

    return quantidade_itens / capacidade


# Exemplo: 3 itens armazenados em uma tabela com capacidade para 8 posições
fc = fator_de_carga(quantidade_itens=3, capacidade=8)
print(f"Fator de carga: {fc:.3f} ({fc:.1%})")