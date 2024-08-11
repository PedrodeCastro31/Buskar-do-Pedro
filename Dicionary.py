# Uma estrutura de conteúdo de Dicionary funciona com uma atribuição de chave(Apelido) para uma porta(Nome Completo).
# Apesar de parecer desorganizada, considerando que a ordem não é relevante, esse tipo de estrutura é extremamente prático, no que
# a velocidade para encontrar informações não muda quando a lista aumenta de tamanho. Um exemplo na vida real é uma barra de pesquisa
# (Apesar de não ser exatamente uma estrutura dicionary, uma barra de pesquisa se assemelha e pode ser criada com essa estrutura).

class Dicionary:

    def __init__(self):
        self.itens =  []

    def vazia(self):
        return len(self.itens) == 0
    
    def adicionar(self, item):
        self.itens.append(item)

    def remover(self, item):
        if self.vazia():
           print("O Dicionary está vazio")
        else:  
            self.itens.pop(item)

    def view_dicionary(self):
        if self.vazia():
            print("O Dicionary está vazio")
        else:
            self.itens
    
    def ind_dicionary(self, item):
        



