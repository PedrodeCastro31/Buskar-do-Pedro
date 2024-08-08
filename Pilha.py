#Pilha: É uma estrutura em que você literalmente empilh os elementos. O último a entrar vai ser o primeiro a sair. Um exemplo pode ser
#uma pilha de camisetas.
class Pilha:
    def __init__(self):
        self.itens = []

    def vazia(self):
        return len(self.itens) == 0

    def empilhar(self, item):
        self.itens.append(item)

    def desempilhar(self):
        if not self.vazia():
            return self.itens.pop()
        else:
            return "A pilha está vazia!"

    def topo(self):
        if not self.vazia():
            return self.itens[-1]
        else:
            return "A pilha está vazia!"
        
pilha = Pilha()

while True:

    comando = input("Digite 'Empilhar', 'Desempilhar', ou 'Topo'")

    if comando == 'Empilhar':
        item = input("O que você quer empilhar?")
        empilhar = pilha.empilhar (item)
        print(f'{item} empilhado(a).')

    elif comando == 'Desempilhar':
        desempilhar = pilha.desempilhar()
        print(f"{desempilhar} desempilhado(a)")

    elif comando == 'Topo':
        topo = pilha.topo()
        print(f'{topo}')
    else:
        break
