n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
om = input('Digite a operação desejada (+, -, *, /): ')
if om == '+':
    print(f'{n1} + {n2} = {n1 + n2}')
elif om == '-':
    print(f'{n1} - {n2} = {n1 - n2}')
elif om == '*':
    print(f'{n1} * {n2} = {n1 * n2}')
elif om == '/':
    print(f'{n1} / {n2} = {n1 / n2}') #ou print(f'{n1} / {n2} = {n1 // n2}')
   
else: print('Operação inválida.')

#om= variavel operacao matematica n1=numero1 n2=numero2