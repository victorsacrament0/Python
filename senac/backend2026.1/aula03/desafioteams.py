produtos = []
precos = []
pedidos = []

def mensagem(msg):
    print(msg)

def cadastrar_produto(produto, preco):
    produtos.append(produto)
    precos.append(preco)
    return mensagem('Lanche cadastrado')

def mostrar_produto():
    for i in range(len(produtos)):
        mensagem(f'{i+1} - {produtos[i]} - R${precos[i]}')

def fazer_pedido(pedido):
    pedidos.append(precos[pedido])

def calcular_total():
    return sum(pedidos)

def menu():
    print('\n==== Produtos Py ====')
    print('1- Cadastrar Produto \n2 - Mostrar Produtos \n3- Fazer Pedido \n4 - Mostrar Total \n5 - Sair')


def main():
    while True:
        menu()
        opcao = int(input('Escolha uma opção: '))
        if opcao == 1:
            produto = input('Digite o produto: ')
            preco = float(input('Informe o valor: '))
            cadastrar_produto(produto,preco)
            mensagem('Produto Cadastrado com SUCESSO!')

        elif opcao == 2:
            mensagem('\n==== PRODUTOS ====')
            mostrar_produto()

        elif opcao == 3:
            mensagem('\n==== PRODUTOS ====')
            mostrar_produto()
            escolha = int(input('Escolha o produto pelo número: '))
            fazer_pedido(escolha)
            mensagem('Pedido Realizado')

        elif opcao == 4:
            mensagem(f'O total é R${calcular_total}')
            if calcular_total >= 100:
                desconto = calcular_total * 0.10
                calcular_total -= desconto
                print("Desconto aplicado!")     

        elif opcao == 5:
            mensagem('Saindo...')
            break

        else:
            print('Digite um valor valido!')

 



main()