# ====================================== LISTAS SIMPLES LIGADAS ======================================

# class declara um tipo; cada objeto Nodo armazena um dado e uma referência seguinte.
class Nodo:
    def __init__(self, dado):
        # __init__ inicializa a instância; self referencia o objeto recém-criado.
        self.dados = dado  # Atribuição guarda o argumento como atributo da instância.
        self.proximo = None  # None representa que ainda não há próximo nó.

# A classe da lista mantém a referência ao primeiro nó.
class ListaSimplesLigada:
    def __init__(self):
        self.cabeca = None

    # def declara um método; dado é o parâmetro recebido para criar o novo nó.
    def inserir(self, dado):
        novo_nodo = Nodo(dado)
        # not testa se a cabeça ainda não aponta para um nó.
        if not self.cabeca:
            self.cabeca = novo_nodo
            return  # Encerra o método após tratar a lista vazia.
        atual = self.cabeca
        # while repete enquanto existir próximo nó; cada passo avança a referência.
        while atual.proximo:
            atual = atual.proximo
        atual.proximo = novo_nodo

    # Percorre os nós e retorna True se localizar o dado; caso contrário, False.
    def buscar(self, dado):
        atual = self.cabeca
        while atual:
            # == compara o dado armazenado ao valor procurado.
            if atual.dados == dado:
                return True
            atual = atual.proximo
        return False

    # Remove a primeira ocorrência do dado, ajustando a referência do nó anterior.
    def remover(self, dado):
        if not self.cabeca:
            return
        if self.cabeca.dados == dado:
            self.cabeca = self.cabeca.proximo
            return
        atual = self.cabeca
        # and exige que haja próximo nó e que ele não seja o elemento procurado.
        while atual.proximo and atual.proximo.dados != dado:
            atual = atual.proximo
        # Se houver próximo nó, ele é ignorado ao ligar o atual ao seguinte dele.
        if atual.proximo:
            atual.proximo = atual.proximo.proximo

    # Imprime os dados seguindo os nós até a referência None.
    def imprimir(self):
        atual = self.cabeca
        while atual:
            # end altera o final padrão de print (quebra de linha) para uma seta.
            print(atual.dados, end=" -> ")
            atual = atual.proximo
        print("None")