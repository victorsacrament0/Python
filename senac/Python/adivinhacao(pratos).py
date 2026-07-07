print(('_' * 30 ) + '\n')
print('--Jogo da adivinhação--')
print(('_' * 30) + '\n')
print('Descubra o PRATO secreto\n Dentro desta lista:\n macarronada,lasanha,pizza,\n yakisoba,feijoada,parmegiana,\n hamburger,cachorro-quente,bobó')
print(('_' * 30) + '\n')

import random
pratos = ['macarronada','lasanha','pizza','yakisoba','feijoada','parmegiana','hamburger','cachorro-quente','bobó']
p_certo = random.choices(pratos)
tentativa = 5

try:
    while tentativa > 0:
        

        prato = input('Digite um prato: ' ).lower()
        print(f"-Você digitou: ({prato})-")
        print(('_' * 30) + '\n')
        if prato not in [s.lower() for s in pratos]:
            print("Digite um prato válido na lista !")
            continue
        
        if prato == p_certo:
            print('\n')
            print(('- Acertou Miseravi -') + '\n') 
            print(('_' * 30) + '\n')
            break
        elif prato != p_certo:
            print('\n')
            print(('- Quase lá, tente novamente!') + '\n')
            tentativa -= 1
            print(f'Tentativa numero {tentativa} de 5')
            print(('_' * 30) + '\n')
        else:
            print('\n')
            print(('-ERRO-') + '\n')
            print(('_' * 30) + '\n')
            continue
    print(('_' * 30) + '\n')
    print('----O prato era: {} ----'.format(p_certo))
except ValueError:
    print('\n')
    print ('Valor Invalido')
    print(('_' * 30) + '\n')


"""
#Imports primeiro
import random
 
#Declarar lista
menu = ["Lasanha", "Feijoada", "Churrasco", "Pizza", "Strognof"] #Criamos a lista
prato_secreto = random.choice(menu).lower() #Seleciona um iten da lista
 
tentativas = 5
 
#Enfeite do pavão
print("== Descubra o prato secreto do Chef ==")
print(f"Você possui {tentativas} tentativas.\n")
print(20 * "-")
 
try:
    while tentativas > 0:
        adivinha_prato = input("Digite o nome do prato: ").lower()
       
        if adivinha_prato == prato_secreto:
            print("Parabéns! Você Acertou.")
            break #Encerra o jogo
        else:
            #Diminuir a tentativa
            #tentativas = tentativas - 1
            tentativas -= 1
            print("Você errou!")
            print(f"Você ainda tem: {tentativas} tentativas ")
 
    #Exibe o prato escolhodo aleatorio pelo jogo        
    print(f"O prato secreto do chef é: {prato_secreto}")
 
except ValueError:
    print("Opçao invalida! ")
"""