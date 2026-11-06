# ====================================== COLISÕES ======================================

class Cliente:
    def __init__(self, cpf, nome):
        self.cpf = cpf
        self.nome = nome

    def __hash__(self):
        return 100

    def __eq__(self, outro):
        if isinstance(outro, Cliente):
            print(f" 🔍Método __eq__ chamado! Comparando CPF {self.cpf} com {outro.cpf}")
            return self.cpf == outro.cpf
        return False

    def __repr__(self):
        return f"Cleinte({self.cpf}, {self.nome})"

banco_dados = {}

c1 = Cliente("111.111.111-11", "Ana")
c2 = Cliente("222.222.222-22", "Bruno")

print("1. Inserindo Cleinte 1 (Ana)...")
banco_dados[c1] = "Conta Ativa"

print("\n2. Inserindo Cliente 2 (Bruno - Mesma Posição hash!)...")
banco_dados[c2] = ""

print("\n3. Buscando Cliente 1...")
print("Resultado: ", banco_dados[c1])