print(('_' * 30 ) + '\n')
print('--Jogo da adivinhação--')
print(('_' * 30) + '\n')
print('Descubra o valor secreto')
print(('_' * 30) + '\n')

n_certo = 11

try:
    num = int(input('Digite um numero inteiro: ' ))
    print(f"-Você digitou: ({num})-")
    print(('_' * 30) + '\n')
   
    if num == n_certo:
        print('\n')
        print(('- Acertou Miseravi -') + '\n') 
        print(('_' * 30) + '\n')
    elif num < n_certo:
        print('\n')
        print(('- Quase lá, mas este valor ainda é menor que o desejado!-') + '\n')
        print(('_' * 30) + '\n')
    else:
        print('\n')
        print(('- Quase lá, mas este valor é maior que o desejado!-') + '\n')
        print(('_' * 30) + '\n')
except ValueError:
    print('\n')
    print ('Valor Invalido')
    print(('_' * 30) + '\n')

  
    # try - except - servem para fazer tratamento de erros