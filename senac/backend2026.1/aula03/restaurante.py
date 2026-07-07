lanches = []
precos = []
pedidos = []

def mensagem(msg):
    print(msg)

def cadastrar_lanche(lanche, preco):
    lanches.append(lanche)
    precos.append(preco)
    return mensagem('Lanche cadastrado')

def mostrar_cardapio():
    for i in range(len(lanches)):
        mensagem(f'{i+1} - {lanches[i]} - R${precos[i]}')

def fazer_pedido(pedido):
    pedidos.append(precos[pedido])

def calcular_total():
    return sum(pedidos)

def menu():
    print('\n==== Lanchonete ====')
    print('1- Cadastrar Lanche \n2 - Mostrar Cardápio \n3- Fazer Pedido \n4 - Mostrar Total \n5 - Sair')


def main():
    while True:
        menu()
        opcao = int(input('Escolha uma opção: '))
        if opcao == 1:
            lanche = input('Digite o lanche: ')
            preco = float(input('Informe o valor: '))
            cadastrar_lanche(lanche,preco)
            mensagem('Lanche Cadastrado com SUCESSO!')

        elif opcao == 2:
            mensagem('\n==== CARDAPIO ====')
            mostrar_cardapio()

        elif opcao == 3:
            mensagem('\n==== CARDAPIO ====')
            mostrar_cardapio()
            escolha = int(input('Escolha o lanche pelo número: '))
            fazer_pedido(escolha)
            mensagem('Pedido Realizado')

        elif opcao == 4:
            mensagem(f'O total é R${calcular_total}')  

        elif opcao == 5:
            mensagem('Saindo...')
            break

        else:
            print('Digite um valor valido!')
              
main()