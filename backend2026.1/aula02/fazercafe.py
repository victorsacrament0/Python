#função criada
def fazer_cafe():
    print('Café Pronto!')

#como chamar a função

fazer_cafe()


""" crie uma funcao que mostre a mensagem """

def msg():
    print('Bem Vindo ao sistema!')

msg()


""" Crie Funões chamadas saudacao, menu e linha """

def saudacao():
    print('Saudações!')
def menu():
    print('Menu:','\n','Macarronada e Feijoada')
def line():
    print('_'*30,'\n')

saudacao()
menu()
line()

""" Faça uma função que mostre o nome de um aluno """
id = input('Digite o seu nome:')

def saudacao(id):
    
    print(f'Olá, {id}!')
 
saudacao(id)

""" Outros Desafios """

age = input('Digite a idade:')
city = input('Digite uma cidade:')
prod = input('Digite um produto:')

def idade(age):
    
    print(f'Idade:{age}')
    print(30*'_')

def cidade(city):
    
    print(f'Cidade:{city}')
    print(30*'_') 

def product(prod):
    
    print(f'Produto:{prod}')
    print(30*'_') 

idade(age)
cidade(city)
product(prod)


""" desafio facil - crie uma funcao que receba nome e idade , mostre """


name = input('Digite seu nome:')
age = input('Digite sua idade:')

def ident(name,age):   
    
    print(f'O aluno {name}, tem {age} anos!')
    print(30*'_','\n')

ident(name,age)