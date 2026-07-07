class Jogo:
    def __init__(self,nome_jogo,cat_jogo,preco_jogo):
        self.nome = nome_jogo
        self.categ = cat_jogo
        self.preco = preco_jogo

    def mostrar_dados(self):
        print(f'|Nome: {self.nome}\n|Categoria: {self.categ}\n|Preço: R${self.preco}')