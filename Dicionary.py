# Uma estrutura de conteúdo de Dicionary funciona com uma atribuição de chave(Apelido) para uma porta(Nome Completo).
# Apesar de parecer desorganizada, considerando que a ordem não é relevante, esse tipo de estrutura é extremamente prático, no que
# a velocidade para encontrar informações não muda quando a lista aumenta de tamanho. Um exemplo na vida real é uma barra de pesquisa
# (Apesar de não ser exatamente uma estrutura dicionary, uma barra de pesquisa se assemelha e pode ser criada com essa estrutura).

class Dicionary:

    def __init__(self):
        self.itens =  []

    def vazia(self):
        return len(self.itens) == 0
    
    def adicionar(self, item, chave):
        self.itens.append({chave : item})

    def remover(self, chave):
        if self.vazia():
            print("O Dicionário está vazio")
        else:
            for i in range(len(self.itens)):
                if chave in self.itens[i]:
                    self.itens.pop(i)
                    print(f"Item com a chave '{chave}' removido.")
                    return
            print(f"Chave '{chave}' não encontrada.")

    def view_dicionary(self):
        if self.vazia():
            print("O Dicionário está vazio")
        else:
            print(f"{self.itens}")
    
    def ind_dicionary(self, chave):
        if self.vazia():
            print("O Dicionário está Vazio")
        else:
            for dicionario in self.itens:
                if chave in dicionario:
                    print(f'Item com a chave "{chave}" é: {dicionario[chave]}')
                    return
            print(f"Chave '{chave}' não encontrada.")

dicionary = Dicionary()

while True:

    comando = input("'Adicionar', 'Remover', 'Ver Dicionário', 'Ver item Dicionário'" )

    if comando == 'Adicionar':
        item = input('O que deseja Adicionar? ')
        chave = input('Chave do item: ')
        dicionary.adicionar(item, chave)
        print(f"{item} adicionado com sucesso. {chave} atribuída.")
    
    elif comando == 'Remover':
        chave = input('Chave do item para remoção:')
        dicionary.remover(chave)
        print(f"{item} removido.")
    
    elif comando == 'Ver Dicionário':
        dicionary.view_dicionary()

    elif comando == 'Ver Item Dicionário':
        chave = input("Chave do item:")
        dicionary.ind_dicionary(chave)

    else:
        break


        



