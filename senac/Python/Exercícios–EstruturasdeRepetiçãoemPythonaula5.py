# 1-Mostre na tela os números de 1 a 10 usando for.

for num in range(1,11,1):  #(começo, final , passo(de quanto em quanto, intervalo) )
    print('Valor :' + str(num))
print('_' * 40)

#2-Mostre na tela os números de 10 a 1 (ordem decrescente)

for num in range(10,0,-1):  #(começo, final , passo(de quanto em quanto, intervalo) )  
    print('Valor :' + str(num))
print('_' * 40)

# 3- Exiba a tabuada do número 5 (de 1 a 10)

print('Tabuada do 5:')
for num in range(1,11,1):
    print(f'5 x {num} = {5 * num}')
print('_' * 40)

# 4-Exiba apenas os numeros pares de 1 a 20.

print('Numeros pares de 1 a 20:')   

for num in range(1,21):
    if num % 2 == 0:
        print('Numero par:' + str(num))
print('_' * 40)

# 5-Peça 5 números ao usuário e mostre a soma total.

soma_total = 0
for i in range(5):
    numero = float(input(f"Digite o {i}º número: "))
    soma_total += numero  
print(f"A soma total dos números é: {soma_total}")

"""
v1 = float(input('Digite o primeiro valor: '))
v2 = float(input('Digite o segundo valor: '))
v3 = float(input('Digite o terceiro valor: '))
v4 = float(input('Digite o quarto valor: '))    
v5 = float(input('Digite o quinto valor: '))
soma = v1 + v2 + v3 + v4 + v5
print('_' * 40)
print(f'Valores digitados: {v1}, {v2}, {v3}, {v4}, {v5}')

print(f'Soma dos valores: {soma}')
print('_' * 40)"""

# 6-Peça números ao usuário até que ele digite 0. Ao final, mostre a soma de todos os números digitados.

soma = 0
numero = 1
 
while numero != 0:
    numero = int(input("Informe um numero ou digite 0 para sair: "))
    soma = soma + numero
 
print(f"Soma: {soma} ")


#com o usuario sem saber que o zero para
soma = []
while True:
    num = int(input('Tente acertar o número secreto: '))
     

    if num == 0:
        print('_' * 40)
        print('Acertou o numero 0, programa encerrado! ')
        print('_' * 40)
        break  
    try:
        soma.append(num)  #append é um método de lista que adiciona um elemento ao final da lista. (acrescenta o numero digitado a lista soma)
        
    except ValueError:
     print('_' * 40)
     print('Valor invalido, digite um numero inteiro!')
     print('_' * 40)

total = sum(soma)   # sum =calcula a soma dos elementos de um iterável (listas, tuplas, conjuntos) de forma rápida. 
                    #Ela é ideal para somar números (inteiros ou floats), retornando o total da soma dos itens 
                    # mais um valor opcional inicial(padrão é iniciar em 0)
print(f"Números digitados: {soma}")
print(f"Soma dos números digitados: {total}")

#identação foi bastante usada! tava errando bastante a estrutura.

# 7-Peça a senha ao usuário até que ele acerte (senha = "1234").

senha = input('Digite a senha: ')

while senha != "1234":
    print('Senha incorreta, tente novamente!')
    senha = input('Digite a senha: ')
if senha == "1234":
        print('_' * 40)
        print('Senha correta, acesso permitido!')
        print('_' * 40)


# 8-Mostre a tabuada de um número escolhido pelo usuário.

try:
    print('_' * 40)
    num = int(input('Digite um numero para ver a tabuada: '))
    print('_' * 40)
    print(f'|Tabuada do {num}: |')
    print('_' * 40)
    for i in range(1, 11):
        print(f'{num} x {i} = {num * i}')
except ValueError:
    print('_' * 40)
    print('Por favor, digite um número válido.')
print('_' * 40)

#9 Peça 10 números ao usuário e mostre:

# - o maior número
# - o menor número

#sem lista

numero = int(input("Informe um numero: "))
 
maior = numero
menor = numero
 
for i in range(9):
    numero = int(input("Informe um numero: "))
 
    if numero > maior:
        maior = numero
 
    if numero < menor:
        menor = numero
 
print("Maior", maior)
print("Mwnor", menor)


#com lista
numeros = []
n = 0

print("Digite 10 valores inteiros: ", '\n')
try:
    for n in range (10):
        n = int(input('Digite um valor:'))
        numeros.append(n)
except ValueError:
    print('_' * 40)
    print('Por favor, digite um numero valido.')
print('_' * 40 , '\n')

maior = max(numeros) #MAX - Ela percorre a lista e retorna o elemento numérico ou alfabético de maior valor.
menor = min(numeros)
print (f'Os numeros digitados foram: {numeros}')
print (f'O maior numero digitado foi: {maior}')
print (f'O menor numero digitado foi: {menor}')


#10 Peça números ao usuário até que ele digite 0 e mostre:

#  - quantos números foram digitados
#  - a soma deles
#  - a média

soma = 0
numero = 1
numeros = []  #lista

while numero != 0:
    numero = int(input("Informe um numero ou digite 0 para sair: "))
    soma = soma + numero
    numeros.append(numero)  #adiciona a lista

media = len(numeros) # len é uma ferramenta nativa usada para retornar o número de itens(o comprimento)
                     #       de um objeto, como strings, listas, tuplas, dicionários ou conjuntos

print(f'Números digitados: {numeros}') 
print(f"Soma: {soma} ")
print(f'Media:{soma / (media-1) }')



# 11-Crie um programa que mostre todos os números pares entre dois números informados pelo usuário.

while True:

    try:
        print('_' * 40)
        n1 = int(input('Digite o primeiro numero: '))
        n2 = int(input('Digite o segundo numero: '))
        print('_' * 40)

        if n1 > n2:
            n3 = n1 #Guarda o valor de 1
            n1 = n2 #Troca o valor de 1 para o do 2
            n2 = n3  #Troca o valor de 2 para 3
        print(f'|Números pares entre {n1} e {n2}: |')
        print('_' * 40)

        for i in range(n1, n2 + 1):
            if i % 2 == 0:
                print(i)
        print('_' * 40)       
        break 

    except ValueError:
     print('_' * 40)
     print('Por favor, digite um número válido.')

#12 Simule uma votação com 5 pessoas. Pergunte o voto (1,2 e 3) e mostre no final qual opção teve mais votos

voto1 = 0
voto2 = 0
voto3 = 0

print('_'*50, '\n')
print("Início da Votação para presidente do SenacRJ", '\n')
print('_'*50)
print("Opções: \n[1] Candidato Zé , [2] Candidato Zi, [3] Candidato Zó")
print('_'*50)


for i in range(1, 6):
    while True:
        try:
            voto = int(input(f"Pessoa {i}, digite seu voto (1-3): "))
            if 1 <= voto <= 3:
                break
            else:
                print("Voto inválido. Tente novamente.")
        except ValueError:
            print("ERRO. Digite apenas números 1, 2 ou 3.")

    if voto == 1:
        voto1 += 1
    elif voto == 2:
        voto2 += 1
    elif voto == 3:
        voto3 += 1

print('_'*50)
print("Resultado Final:", '\n')

print(f"  Zé: {voto1} voto(s)")
print(f"  Zi: {voto2} voto(s)")
print(f"  Zó: {voto3} voto(s)")

# Determina o vencedor
max_votos = max(voto1, voto2, voto3)     #retorna o maior item em um iterável (lista, tupla, conjunto) ou o maior entre dois ou mais argumentos             

print('_'*50)
print("   Vencedor(es)    ")

if voto1 == max_votos:
    print("--- Zé venceu ---")
if voto2 == max_votos:
    print("--- Zi venceu ---")
if voto3 == max_votos:
    print("--- Zó venceu ---")
print('_'*50)    