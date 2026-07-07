
# O que são loops ou repetição?
# São comandos que permitem executar um bloco várias vezes.

#Tipos de estrutura de repetição no Python
    # While -> Repente enquanto uma condição for verdadeira.
    # For -> Repete Um numero determinada vezes.

#Estrutura de Wile
#Exemplo 01
print("Exemplo 01")
volta_carrossel = 0

while volta_carrossel <= 5:
    print("Volta no carrosel nº ", volta_carrossel )

    #Iteirando em 1
    #volta_carrossel = volta_carrossel + 1
    volta_carrossel += 1

#Exemplo 02

print("\nExemplo 02")

senha = ""
while senha != "1234":
    senha = input("Informe a senha: ")

print("Acesso Liberado!")

# Estrutura For
# range(inicio, fim, passo) - passo quanto vale a volta
print("\nEstrutura do For")

#Conta de 0 a 4
print("\nPirneiro exemplo:")
for variavel in range(5):    
    print("O valor é: ", variavel)


#Segundo exemplo
#Conta de 1 a 4
print("\nSegundo exemplo:")
for v in range(1,5):
    print("Valor é: ", v)


#Terceiro exemplo
print("Terceiro exemplo:")
for i in range(0,11,2):
    print("O valor é: ", i)

#Comandos de controle
    # break -> para a execução do loop imediamente
    # continue -> Pula a repetição atual e vai para a proxima

# Exemplo break

print("\n Exemplo do break")
for i in range(10):
    if i == 8:
        break
    print(i)

# Exemplo continue
print("Exemplo continue")

for i in range(5):
    if i == 3:
        continue
    print(i)



# Percorrer uma lista 
lista_prod = ['colher','faca','garfo','panela','frigideira']

for prod in lista_prod:
    print(prod)

# transformar toda palavra dentro da lista ficar com a 1 letra em maiusculo

lista_prod = ['colher','faca','garfo','panela','frigideira']

for prod in lista_prod:
    print(prod.capitalize())  #capitalize é utilizado para formatar strings, convertendo o primeiro
                                  #caractere para maiúsculo e todos os caracteres restantes para minúsculos



#Loop ou repetição: São comandos que permitem executar um bloco varias vezes
num = 0

while num < 10:
    print('Decrescente: ' + str(num))
    num += 1

'''----------------------'''
for num in range(0,10,2):  #(começo, final , passo(de quanto em quanto, intervalo) )
    print('Varlor :' + str(num))

# Calcular imposto de produtos e calcular eles (imposto para valores maiores q 1000 de 15% e ate mil 10%)
lista_preco = [1200,1000,1500,800]
total_imposto = 0

for preco in lista_preco:
    if preco > 1000:
        taxa = 0.15
    else:
        taxa = 0.1
    imposto = taxa * preco

    total_imposto += imposto
    print(f'Valor do produto: {preco} com imposto de {imposto}')

print('Total dos impostos é', total_imposto )


#Usar o for num dicionario: calcular o percentual de crescimento
#calculo valor / valor2 - 1 - procentagem de crescimento de um ano pro outro

vendas23 = {'jan': 15000, 'fev':12000,'mar':13500}
vendas24 = {'jan': 16000, 'fev':13000,'mar':12000}

for mes in vendas24:
    valor23 = vendas23[mes]
    valor24 = vendas24[mes]
    crescimento = valor24 / valor23 - 1
    print(f'No mes de {mes} o crescimento foi de {crescimento:.1%}') 
                                             #.1% retorna quantas casas vc quer dps do . e % o tipo que deseja


