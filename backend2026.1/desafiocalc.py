class Calculadora:
    def __init__(self):
        print('|:.Calculadora Python.:|')

    def somar (self,nu1,nu2):
        print (f"\n|:Resultado: {nu1} + {nu2} = {nu1 + nu2}:|\n")
    
    def subtrair (self,nu1,nu2):
        print(f"\n|:Resultado: {nu1} - {nu2} = {nu1 - nu2}:|\n")
    
    def dividir (self,nu1,nu2):
        print(f"\n|:Resultado: {nu1} ÷ {nu2} = {nu1 / nu2}:|\n")

    def multiplicar (self,nu1,nu2):
        print(f"\n|:Resultado: {nu1} x {nu2} = {nu1 * nu2}:|\n")
        

    def main(self):
        
        while True:
            opcao = int(input("Escolha um opção:(Para sair, digitar qualquer outro valor)\n[1 - Somar]\n[2 - Subtrair]\n[3 - Dividir]\n[4 - Multiplicar]\n ->"))
 
            if opcao == 1:
                number1 = float(input('Digite o primeiro número: '))
                number2 = float(input('Digite o segundo número: '))
                self.somar(number1,number2)
            elif opcao == 2:
                number1 = float(input('Digite o primeiro número: '))
                number2 = float(input('Digite o segundo número: '))
                self.subtrair(number1,number2)
            elif opcao == 3:
                number1 = float(input('Digite o primeiro número: '))
                number2 = float(input('Digite o segundo número: '))
                self.dividir(number1,number2)
            elif opcao == 4:
                number1 = float(input('Digite o primeiro número: '))
                number2 = float(input('Digite o segundo número: '))
                self.multiplicar(number1,number2)
            else:
                print(f"\n| VALOR INVALIDO |\n")
                break




numero = Calculadora()
numero.main()
