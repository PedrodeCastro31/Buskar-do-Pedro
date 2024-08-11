# Fila: É uma estrutura onde o primeiro item adcionado é o primeiro a sair. Um exemplo na vida real pode ser um pedágio, onde o
# primeiro carro da fila será o primeiro a pagar e passar pelo pedágio.

class Fila:
    
    def __init__(self):
        self.itens = []

    def vazia(self):
        return len(self.itens) == 0
    
    def adcionar(self, item):
        self.itens.append(item)

    def remover(self):
        if self.vazia == True:
            return "Não tem ninguém na Fila :("
        else:
            return self.itens.pop(0)
    
    def frente(self):
        if self.vazia == True:
            return "Não tem ninguém na Fila :("
        else:
            return self.itens[0]

fila = Fila() 

while True:
    comando = input("'Adcionar', 'Remover' ou 'Frente' ")

    if comando == 'Adcionar':
        item = input("O que deseja Adcionar a Fila? ")
        fila.adcionar (item)
        print(f"{item} adcionado(a).")

    elif comando == 'Remover':
        if fila.vazia():
            print(f"A fila Está Vazia")
        else:
            remover = fila.remover()
            print(f"{remover} removido(a).")
    
    elif comando == 'Frente':
        if fila.vazia():
            print(f"A fila está Vazia")
        else:
            frente = fila.frente()
            print(f"{frente} é o primeiro(a) da fila.")

    else:
        break

        
