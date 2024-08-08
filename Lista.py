#Lista são formas de organizar informações sem uma ordem de saída específica. Um exemplo na vida real pode ser uma Lista de Compras 
#de peças automotivas, onde eu posso adcionar itens numa ordem específica e retirar qualquer um na ordem que eu quiser.

class Lista:

    def __init__(self):
        self.itens = []

    def vazia(self):
        return len(self.itens) == 0
    
    def adcionar(self, item):
        self.itens.append(item) 

    def remover(self, item):
        if self.vazia():
            print('A lista está vazia.')
        elif item in self.itens:
            self.itens.remove(item)
        else: print(" o item não está na lista")

    def ver_lista(self):
        if self.vazia():
            print('A lista está vazia.')
        else: 
            return self.itens
        
lista = Lista()
    
while True:

    comando = input("'Adcionar', 'Remover', 'Lista' ")

    if comando == 'Adcionar':
        item = input('O que você quer adcionar? ')
        lista.adcionar (item)
        print(f"{item} adcionado(a).")  
    
    elif comando ==  'Remover':
        if lista.vazia():
            print(' A lista está vazia')
        else:
            item = input('O que você quer remover? ')
            if item in lista.itens:
                lista.remover (item)
                print("Item removido com sucesso.")
            else: print('O item não está na lista.')
    
    elif comando == 'Lista':
        if lista.vazia():
            print('A lista está Vazia')
        else:
            ver = lista.ver_lista()
            print(f"{ver}")
    
    else:
        break

