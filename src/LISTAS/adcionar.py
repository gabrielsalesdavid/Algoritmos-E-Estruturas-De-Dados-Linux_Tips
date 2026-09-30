print("🛒 BEM-VINDO AO SISTEMA DE CARRINHO DINÂMICO 🛒")

# 1. Iniciamos nossa lista vazia (um carrinho de compras pronto para ser preenchido)
carrinho = []

# --- FASE 1: INSERÇÃO DINÂMICA ---
# Criamos um loop infinito para o usuário digitar quantos itens quiser
while True:
    produto = input("Digite o nome do produto (ou '0' para finalizar): ")
    
    # Nossa condição de parada. Se digitar '0', o break quebra o loop!
    if produto == '0':
        print("\nFinalizando as compras... Gerando o recibo...\n")
        break
        # exit()  # Poderíamos usar exit() para encerrar o programa, mas vamos apenas quebrar o loop
        
    # Se não quebrou o loop, adicionamos o produto no final da lista
    carrinho.append(produto)
    print(produto + " adicionado com sucesso!")


# --- FASE 2: ITERAÇÃO E LEITURA ---
print("🧾 SEU RECIBO DE COMPRAS 🧾")

# Verificamos se o usuário comprou algo (se o tamanho da lista é maior que zero)
if len(carrinho) == 0:
    print("Seu carrinho está tristemente vazio. Vá comprar algo!")
else:
    # Criamos nossa variável contadora que servirá como Índice
    i = 0
    
    # O loop vai rodar do índice 0 até o último índice válido (tamanho da lista - 1)
    while i < len(carrinho):
        # Acessamos o elemento da lista usando a variável 'i'
        item_atual = carrinho[i]
        
        # Imprimimos de forma amigável para humanos (índice + 1)
        print("Item " + str(i + 1) + ": " + item_atual)
        
        # A engrenagem vital do loop: aumentamos o índice para ir ao próximo vagão
        i += 1

print("\nObrigado por usar nosso sistema!")