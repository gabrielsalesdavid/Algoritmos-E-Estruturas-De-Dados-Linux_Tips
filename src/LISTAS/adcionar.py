# print() exibe uma mensagem literal, incluindo caracteres Unicode.
print("🛒 BEM-VINDO AO SISTEMA DE CARRINHO DINÂMICO 🛒")

# Colchetes vazios criam uma lista vazia; ela receberá os produtos.
carrinho = []

# --- FASE 1: INSERÇÃO DINÂMICA ---
# while True cria um laço contínuo; break será usado para sair dele.
while True:
    # input() mostra a solicitação e retorna o texto digitado pelo usuário.
    produto = input("Digite o nome do produto (ou '0' para finalizar): ")
    
    # if verifica a condição; == compara strings; break encerra o laço mais interno.
    if produto == '0':
        print("\nFinalizando as compras... Gerando o recibo...\n")
        break
        # exit()  # Poderíamos usar exit() para encerrar o programa, mas vamos apenas quebrar o loop
        
    # Se a condição de parada não ocorreu, append() acrescenta o texto à lista.
    carrinho.append(produto)
    print(produto + " adicionado com sucesso!")


# --- FASE 2: ITERAÇÃO E LEITURA ---
print("🧾 SEU RECIBO DE COMPRAS 🧾")

# len() retorna a quantidade; == 0 testa se a lista está vazia.
if len(carrinho) == 0:
    print("Seu carrinho está tristemente vazio. Vá comprar algo!")
else:
    # else executa quando a condição do if é falsa; i servirá como índice.
    i = 0
    
    # O laço continua enquanto i for menor que o tamanho da lista.
    while i < len(carrinho):
        # Colchetes acessam o item na posição i (índices começam em zero).
        item_atual = carrinho[i]
        
        # str() converte i+1 para texto antes da concatenação com outras strings.
        print("Item " + str(i + 1) + ": " + item_atual)
        
        # += atualiza i somando 1, permitindo avançar para o próximo item.
        i += 1

print("\nObrigado por usar nosso sistema!")