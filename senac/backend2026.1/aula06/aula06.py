class Animal:
    def __init__(self,nome_animal,idade_animal,tipo_animal):
        self.nome = nome_animal
        self.idade = idade_animal
        self.tipo = tipo_animal

    def mostrar_dados(self):
        print(f'|Nome: {self.nome}\n|Idade: {self.idade}\n|Tipo: {self.tipo}')

 
 
class Petshop:
    def __init__(self):
        self.animais = []
        print('\n==== ANIMAIS ====')
   
    def cadastar_animal(self,nome,idade,tipo):
        meu_animal = Animal(nome,idade,tipo)
        self.animais.append(meu_animal)
        print('_'*25)
        print(' - Animal Cadastrado! -')
        print('_'*25,'\n')

    def mostrar_animais(self):
        print('_'*45)
        
        for meu_animal in self.animais:
            meu_animal.mostrar_dados()
            print('_'*45,'\n')
        

    def main(self):
         
        while True:
            try:
                opcao = int(input("Escolha um opção:\n[1 - Cadastrar]\n[2 - Mostrar]\n[3 - Sair]\n ->"))
                
                if opcao == 1:
                    nameani = input('Digite o nome: ')
                    ageani = input('Digite a idade: ')
                    typeani = input('Qual o tipo: ')
                    self.cadastar_animal(nameani,ageani,typeani)
                elif opcao == 2:
                     self.mostrar_animais()
                elif opcao == 3:
                    print("\nSaindo. Até logo!")
                    break
            except ValueError:
                    print(46*("-"))
                    print("Operação inválida! Por favor, tente novamente.")
                    print(46*("-"))


anim = Petshop()
anim.main()