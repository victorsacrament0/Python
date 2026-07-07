

def calc(valor1, valor2, opm):
    if opm in ['+', 'mais', 'somar', 'soma']:
        resutado = valor1 + valor2
        return resutado
    elif opm in ['-', 'menos', 'subtrair']:
        resutado = valor1 - valor2
        return resutado
    elif opm in ['x', 'multiplica', 'multiplicar']:
        resutado = valor1 * valor2
        return resutado
    elif opm in ['/', 'dividir', 'divisao', 'divisão']:
        if valor2 == 0:
           mensagem = "Não é possivel divisão por ZERO"
           return mensagem
        else:
            resutado = valor1 / valor2
            return resutado
        
def main():    
    valor1 = int(input('Digite um valor inteiro positivo: '))
    valor2 = int(input('Digite outro valor inteiro positivo: '))
    opm = input('Digite a operação matematica desejada: ').lower()    
    
    print(f'O resultado é : {calc(valor1, valor2, opm)}')

main()