print(('_' * 30 ) + '\n')
print('--Jogo da adivinhação--')
print(('_' * 30) + '\n')
print('Descubra o valor secreto')
print(('_' * 30) + '\n')

import random

try:

    n_certo = random.randint(10,100)

    num = int(input('Digite um numero entre 10 e 100: ' ))
    print(f"-Você digitou: ({num})-")
    print(('_' * 30) + '\n')
   
    if num < 10 or num > 100:
        print(f"[ERRO] Tente um número entre 10 e 100. Digitado:({num})")
    elif num == n_certo:
        print('\n')
        print(('- Acertou Miseravi -') + '\n') 
        print(('_' * 30) + '\n')
    elif num < n_certo:
        print('\n')
        print((f'- Quase lá, este valor ainda é menor que o desejado!- R:({n_certo})') + '\n')
        print(('_' * 30) + '\n')
    else:
        print('\n')
        print((f'- Quase lá, este valor é maior que o desejado!- R:({n_certo})') + '\n')
        print(('_' * 30) + '\n')
except ValueError:
    print('\n')
    print ('Valor Invalido')
    print(('_' * 30) + '\n')

  
    # try - except - servem para fazer tratamento de erros
    # RANDOM: começar sempre com import random (importar a biblioteca do random)
    # -random.randrange(0,5) = 0,1,2,3 e 4
    #
    # -random.randint(0,5) = 0,1,2,3,4 e 5
    #
    # -random.choices(variaveis) seleciona múltiplos elementos aleatórios de uma sequência (lista, tupla, etc.) com reposição  
    #                       pode repetir o numero randomico selecionado, ou seja, pode haver repetições. Exemplo: [2, 4, 1, 2]
    # -random.shuffle(variaveis) rearranja os elementos da lista fornecida em uma ordem aleatória. (pega a variavel e embaralha por completo)
    #
    # -random.sample  é utilizada para selecionar aleatoriamente um número específico de itens únicos de uma sequência
    #              sem reposição, ou seja, sem repetir os elementos selecionados.(Diferente do random.coiches)
    #
    # -random.random  é utilizada para gerar um número de ponto flutuante (float) 
    #             pseudo-aleatório no intervalo de 0.0 (inclusive) a 1.0 (exclusivo), ou seja, [0.0, 1.0)
    #
    # -random.uniform(4,10)  é utilizada para gerar um número de ponto flutuante (float) em um intervalo específico, ou seja, 
    #      entre 4.0 e 10.0 (inclusive).
    #  , k=3 = quantidade de elementos a serem selecionados, se for 1, retorna um único elemento, se for maior que 1, 
    #          retorna uma lista com os elementos selecionados. (random.randint(0,5), k=3) = seleciona 3 números aleatórios 
    #          entre 0 e 5, podendo haver repetições. Exemplo: [2, 4, 1]
    # .2f = indica que o número deve ser exibido com 2 casas decimais