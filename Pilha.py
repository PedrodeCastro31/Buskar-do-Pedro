#Pilha: É uma estrutura em que você literalmente empilha os elementos. O último a entrar vai ser o primeiro a sair e vice versa. Um
#exemplo pode ser um caminhão guincho que está levando 3 carros. É impossível tirar o primeiro carro sem tirar os outros dois, por
#isso ele é o último a sair da "pilha".

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
        if pilha.vazia():
            print("A pilha está vazia")
        else:
            desempilhar = pilha.desempilhar()
            print(f"{desempilhar} desempilhado(a)")

    elif comando == 'Topo':
        if pilha.vazia():
            print("A pilha está vazia")
        else:
            topo = pilha.topo()
            print(f'{topo}')
    else:
        break
