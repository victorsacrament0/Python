from jogos import Jogo

class Loja:
    def __init__(self):
        self.jogos = []
        print('\n==== Loja de Jogos 3kg ====')
   
    def cadastar_jg(self,nome,categ,preco):
        meu_jogo = Jogo(nome,categ,preco)
        self.jogos.append(meu_jogo)
        print('_'*25)
        print(' - Jogo Cadastrado! -')
        print('_'*25,'\n')

    def mostrar_jogos(self):
        print('_'*45)
        
        for meu_jogo in self.jogos:
            meu_jogo.mostrar_dados()
            print('_'*45,'\n')
    
    def main(self):
         
        while True:
            try:
                opcao = int(input("Escolha um opção:\n[1 - Cadastrar]\n[2 - Mostrar]\n[3 - Sair]\n ->"))
                
                if opcao == 1:
                    namegame = input('Digite o nome: ')
                    catgame = input('Digite a categoria: ')
                    valgame = float(input('Qual o valor: '))
                    self.cadastar_jg(namegame,catgame,valgame)
                elif opcao == 2:
                     self.mostrar_jogos()
                elif opcao == 3:
                    print("\nSaindo. Até logo!")
                    break
            except ValueError:
                    print(46*("-"))
                    print("Operação inválida! Por favor, tente novamente.")
                    print(46*("-"))