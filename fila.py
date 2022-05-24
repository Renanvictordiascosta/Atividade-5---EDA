# Classes para implementar as Filas
# Implementação da classe que será utilizada como elemento da fila
class Elemento:
    def __init__(self, valor, prioridade):
        self.item = valor
        self.prioridade = prioridade

    def __str__(self):
        return str(self.item) + " " + str(self.prioridade)

# Implementação da classe fila
class FilaDePrioridade:

# Inicia uma fila vazia
    def __init__(self):
        self.itens = []

# Verifica se a fila está vazia
    def esta_vazia(self):
        return self.itens == []

# Retorna o número de elementos da fila
    def tamanho(self):
        return len(self.itens)

# Adiciona um elemento no final da fila, com sua prioridade
    def inserir(self, item, prioridade):
        elemento = Elemento(item, prioridade)
        self.itens.insert(0, elemento)
        print("E %s" %elemento)


# Remove o elemento com maior prioridade
    def remover(self):
        if self.esta_vazia():
            print("Está vazia!")

        else:
            posicao = 0
            menor = self.itens[posicao].prioridade
            # Encontra o elemento de maior prioridade
            for i in range(self.tamanho()):
                if self.itens[i].prioridade < menor:
                    posicao = i
                    menor = self.itens[i].prioridade

            # Remove elemento da fila
            removido = self.itens.pop(posicao)

            return removido.itens

    # Imprime com base na prioridade
    def print_fila(self):
        lista = []
        for x in self.itens:
            lista.append(x.item)
        print(lista)
