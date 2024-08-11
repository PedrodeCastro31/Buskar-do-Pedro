# Um Array é uma estrutura que armazena valores do mesmo tipo em uma sequência ordenada onde cada Número pode ser acessado por um índice.
# Um exemplo na vida real pode ser uma tabela de uma concessionária. (Os arrays são bem parecidos com Listas).

class Array():

    def __init__(self):
        self.itens = []

    def vazia(self):
        return len(self.itens) == 0

    def adicionar(self, item):
        self.itens.append(item)

    def remover(self, posicao):
        if self.vazia():
            print("O Array está vazio")
        else:
            if 0 <= posicao < len(self.itens):  
                self.itens.pop(posicao)
            else:
                print("Posição inválida.")

    def ver_array(self):
        if self.vazia():
            print("O Array está vazio")
        else:
            print(f"{self.itens}")

    def individual_array(self, posicao):
        if self.vazia():
            print("O Array está vazio")
        else:
            if 0 <= posicao < len(self.itens):  
                return self.itens[posicao]  
            else:
                return "Posição inválida."

array = Array()

while True:
    comando = input(" 'Adicionar', 'Remover', 'Ver Array', 'Ver Item Individual'. ")

    if comando == 'Adicionar':
        item = input('O que você quer Adicionar? ')
        array.adicionar(item)
        print(f"{item} adicionado.")

    elif comando == 'Remover':
        item = input('Qual é a posição do item que você deseja retirar? ')
        item_int = int(item)
        array.remover(item_int)
        print("Item removido.")

    elif comando == 'Ver Array':
        array.ver_array()

    elif comando == "Ver Item Individual":
        item = input('Qual é a posição do item que você deseja ver? ')
        item_int = int(item)
        individual = array.individual_array(item_int)
        print(f'{individual}')

    else:
        break



