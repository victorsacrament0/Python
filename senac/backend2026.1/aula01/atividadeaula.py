total = 0
mine = 0
gta = 0
fifa = 0
valor_mine = 80
valor_gta = 120
valor_fifa = 90



print('-----Seja bem vindo!------')
print('-Loja de Games Python-')
print('_' * 30 + '\n' )
print('Nossos Jogos: \n Minecraft - R$80 \n GTA V - R$120 \n FIFA - R$90  \n Digite [fim] para finalizar')
print('_' * 30 + '\n' )
try:
    while True:
        pedido = input("\n-Digite o jogo desejado ou digite [fim] para finalizar: ").lower()
        print('_' * 30 + '\n' )
        if pedido in ['fim' , 'finalizar' , 'sair']:
            break
        if pedido in ['minecraft','mine','minicraft','minecreft']:
            qtd = int(input('Digite a quantidade desejada: '))
            total += valor_mine * qtd
            mine += qtd
        elif pedido in ['gta', 'gtav','gta v', 'v']:
            qtd = int(input('Digite a quantidade desejada: '))
            total += valor_gta * qtd
            gta += qtd
        elif pedido in ['fifa' , 'futebol', 'fc']:
            qtd = int(input('Digite a quantidade desejada: '))
            total += valor_fifa * qtd
            fifa += qtd
        else:
            print('Valor Invalido')
        print ('\nItem(ns) adicionado(s)')    
        print(f'O pedido está dando = {total:.2f}')
except ValueError:
        print('\n')
        print ('Valor Invalido')
        print(('_' * 30) + '\n')

if total >= 200:
     valdesc = total - total * 0.1
     desconto = total * 0.1


print(f'Itens comprados: \n Minecraft: {mine} \n GTA V: {gta} \n Fifa: {fifa} \n')

print(f'Valor total do pedido = [R${total:.2f}] \n')
if total >= 200:
    print(f'Valor do desconto [R${desconto:.2f}] \n')
    print('_' * 30 + '\n' )
    print(f'Valor com desconto [R${valdesc:.2f}] \n')
    
else:
    print('Sem desconto') 
    print(f'Valor total do pedido = [R${total:.2f}] \n')   
print('Obrigado por nos escolher, volte sempre!')
print('_' * 30 + '\n' )


""" Segunda Maneira
 

jogos = ["Minecraft", "GTA V", "FIFA", "PAC MAN"]
precos = [80, 120, 90, 50]
 
total = 0
 

for i in range(len(jogos)):
    print(i, "-", jogos[i],"- R$", precos[i] )
 

for i in jogos:
    escolha = int(input("Escolha o jogo: [0] [1] [2] [3]: "))
    total += precos[escolha]
 
    seguir = input("Deseja escolher outro jogo? [s] [n]").lower()
 
    if seguir in ["s", "sim"]:
        continue
    else:
        break
 
if total > 200:
    desconto = total * 0.10
    total -= desconto
    print("Desconto aplicado!")
 
print(f"Total Final: R${total:.2f}")
 
"""