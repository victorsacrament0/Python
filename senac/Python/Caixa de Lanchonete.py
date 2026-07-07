total = 0
hamburger = 0
refri = 0
batata = 0
valor_refri = 5
valor_ham = 10
valor_btt = 7



print('-----Seja bem vindo!------')
print('-Menu Restaurante Simples-')
print('_' * 30 + '\n' )
print('Nosso cardapio: \n Cardápio: \n Hamburguer - R$10 \n Refrigerante - R$5 \n Batata Frita - R$7  \n Digite [fim] para finalizar')
print('_' * 30 + '\n' )
try:
    while True:
        pedido = input("\n-Digite o item desejado: ").lower()
        print('_' * 30 + '\n' )
        if pedido in ['fim' , 'finalizar' , 'sair']:
            break
        if pedido == 'hamburger':
            qtd = int(input('Digite a quantidade desejada: '))
            total += valor_ham * qtd
            hamburger += qtd
        elif pedido == 'refrigerante':
            qtd = int(input('Digite a quantidade desejada: '))
            total += valor_refri * qtd
            refri += qtd
        elif pedido in ['batata' , 'batata frita' , 'batatafrita']:
            qtd = int(input('Digite a quantidade desejada: '))
            total += valor_btt * qtd
            batata += qtd
        else:
            print('Valor Invalido')
        print ('\nItem(ns) adicionado(s)')    
        print(f'O pedido está dando = {total:.2f}')
except ValueError:
        print('\n')
        print ('Valor Invalido')
        print(('_' * 30) + '\n')

if total >= 20:
     total -= total * 0.1

print(f'Itens comprados: \n Hamburguer: {hamburger} \n Refrigerante: {refri} \n Batata Frita: {batata} \n')

print(f'Valor total do pedido = [R${total:.2f}] \n')

print('Obrigado por nos escolher, volte sempre!')
print('_' * 30 + '\n' )
