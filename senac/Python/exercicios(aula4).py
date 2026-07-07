#1️⃣ Verificar maior de idade
#Peça a idade do usuário e informe se é "Maior de idade" ou "Menor de idade".

idade = int(input('Digite a idade: '))
if idade >= 18:
    print('-Maior de idade-')
else:
    print('-Menor de idade-')


#2️⃣ Número positivo ou negativo
#Peça um número inteiro e informe se ele é positivo, negativo ou zero.

numero = int(input('Digite um número inteiro: '))
if numero > 0:
    print('-Positivo-')
elif numero < 0:
    print('-Negativo-')
else:
    print('-Zero-')

#3️⃣ Verificação de senha
#Crie uma variável senha = "python123". Peça ao usuário para digitar a senha e informe se está correta ou incorreta.

senha_correta = "python123"
senha = input('Digite a senha: ')

if senha == senha_correta: print('-Acertou Miseravi-')
else: print('-Tente outra vez-')

#4️⃣ Par ou ímpar
#Peça um número ao usuário e informe se ele é par ou ímpar.

print('|Par ou Impar|')
num = int(input('Digite um numero: '))  
if num % 2 == 0:
    print('-Par-')
else:
    print('-Impar-')
# Outra forma:
#    num = int(input("Informe um valor: "))
#    resto = num % 2
 
#    if resto == 0:
#        print("O numero é par")
#    else:
#        print("O numero é impar")

# 5️⃣ Classificação de nota
#Peça ao usuário uma nota de 0 a 10 e classifique:
#>= 7 → Aprovado
#>= 5 e < 7 → Recuperação
#< 5 → Reprovado

nota = float(input('Digite a nota: ' ))
if nota >= 7:
    print('-Aprovado-')
elif nota >= 5 and nota < 7:
    print('-Recuperação-')
else:
    print('-Reprovado-')


 #6️⃣ Calculadora simples

print('|Calculadora Simples|')
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
    if n2 == 0:
        print('Divisão por 0 não é possivel')
    else:
     print(f'{n1} / {n2} = {n1 / n2}') #ou print(f'{n1} / {n2} = {n1 // n2}')

else: print('Operação inválida.')


#com match case

match om:
    case '+':
        print(f'Soma: {n1} + {n2} = {n1 + n2}')
    case '-':
        print(f'Subtração: {n1} - {n2} = {n1 - n2}')
    case '*':
        print(f'Multiplicação: {n1} * {n2} = {n1 * n2}')
    case '/':
        print(f'Divisão: {n1} / {n2} = {n1 / n2}')
    case _:
        print('Operação inválida.')




#7️⃣ Dia da semana (match case)
#Peça um número de 1 a 7 e mostre o dia da semana correspondente usando match case.

print('Dia da semana:')

weekday = int(input('Digite um numero de 1 a 7: '))

match weekday:
    case 1:
        print('Domingão')
    case 2:
        print('Segunda, Infelizmente')
    case 3:
        print('Terça-Feira')    
    case 4:
        print('Quarta-Feira')   
    case 5:
        print('Quinta-Feira')
    case 6:
        print('Sexta, Amem!')
    case 7:
        print('Sabadasso')
    case _:
        print('Número inválido. Digite um número de 1 a 7.')

#Quando colocamos o case _ ele funciona como um else, ou seja, se nenhum dos casos anteriores for atendido, ele executa o código dentro do case

#8️⃣ Categoria por idade
#Peça a idade de uma pessoa e classifique:
#0 – 12 → Criança
#13 – 17 → Adolescente
#18 – 59 → Adulto
#60+ → Idoso

print ('|-Faixa etaria:-|  ')

age = int(input('Digite a idade: '))

match age:
    case idade if idade < 0:
        print('-Idade invalida-')
    case idade if idade <= 12:
        print('-Criança-')
    case idade if idade < 18:
        print('-Aborrecente-')
    case idade if idade < 60:
        print('-Adulto-')
    case idade if idade >= 60:
        print('-Idoso-')  
    case _:
        print('invalido')


""" Outra forma de fazer, com IF
age = int(input("Informe a idade: "))

if age < 0:
    print('Idade invalida')

elif age <= 12:
    print('Criança')
elif age <= 17:
    print('Adolescente')
elif age <= 59:
    print('Adulto')
elif age >= 60:
    print('Idoso')    

else:
    print('Parametro invalido')    """

#9️⃣ Sistema de login
#Crie duas variáveis:
#usuario = "admin"
#senha = "1234"
#Peça ao usuário para digitar usuário e senha e informe se o login foi bem-sucedido ou incorreto.

usuario_correto = "admin"
senha_correta = "1234"
print('|Login Simples|')
print('Digite seu usuário e senha para acessar o sistema.')
print('_' * 30 + '\n' )

usuario = input('Digite seu usuário: ')
senha = input('Digite sua senha: ')

if usuario == usuario_correto and senha == senha_correta:   
    print('_' * 30 + '\n' )  
    print('-Login bem sucedido-')
else:
    print('_' * 30 + '\n' )  
    print('-Usuário ou senha incorretos-')

print('_' * 30 + '\n' )


''' Outra forma com if if

usuario_certo = "admin"
senha_certa = "1234"

usuario = input('Digite um usuario: ')
senha = input('Digite uma senha: ')

if usuario == usuario_certo:
    if senha == senha_certa:
        print ("Usuario e Senha corretas")
    else:
        print ("Usuario e(ou) senha invalido(s)")   
else:
        print ("Usuario e(ou) senha invalido(s)")      
'''


#🔟 Menu de restaurante (match case)
# Crie um menu: 1 → Hambúrguer 2 → Pizza 3 → Salada 4 → Refrigerante
#O usuário digita o número do pedido e o programa mostra o item escolhido usando match case.

print('-----Seja bem vindo!------')
print('-Menu Restaurante Simples-')
print('1. Hamburguer')
print('2. Pizza')
print('3. Salada')  
print('4. Regrigerante ')  
print('_' * 30 + '\n' )

pedido = int(input("Digite o numero do pedido: ")) 
print('_' * 30 + '\n' )

match pedido:
    case 1:
        print('Você pediu um Hamburguer')
    case 2: 
        print('Você pediu uma Pizza')
    case 3:
        print('Você pediu uma Salada')
    case 4:
        print('Você pediu um Refrigerante')
    case _:
        print('Pedido inválido. Por favor, escolha um número de 1 a 4.')
        print('_' * 30 + '\n' )

print('Obrigado por nos escolher, volte sempre!')
print('_' * 30 + '\n' )