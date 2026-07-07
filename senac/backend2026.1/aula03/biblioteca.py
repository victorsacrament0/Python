biblioteca = []
emprestimos = []

def mensagem(msg):
    print(msg)

def cadastro_livros():
    nome_livro = input('Nome do Livro: ')
    biblioteca.append(nome_livro)
    mensagem('Livro Cadastrado!')

def mostrar_livros():
    mensagem('\n==== LIVROS ====')
    for i in range(len(biblioteca)):
        mensagem(f'{i+1} - {biblioteca[i]}')

def emprestimo_livros():
    mostrar_livros()
    escolha = int(input('Escolha a opção desejada pelo número: '))
    emprestimos.append(biblioteca[escolha])
    mensagem('Livro emprestado com sucesso!')

def total_emprestimo():
    return len(emprestimos)

def menu():
    print('\n==== Biblioteca Python ====')
    print('1 - Cadastrar Livros')
    print('2 - Mostrar Livros')
    print('3 - Emprestrar Livros')
    print('4 - Total emprestado')
    print('5 - Sair')

def main():
    menu()
    while True:
        opcao = int(input('Escolha uma opção: '))
        if opcao == 1:
            cadastro_livros()

        elif opcao == 2:
            mostrar_livros()

        elif opcao == 3:
            emprestimo_livros()

        elif opcao == 4:
            mensagem(f'Total de emprestimos: {total_emprestimo()}')

        elif opcao == 5:
            mensagem('Saindo...')
            break

        else:
            print('Digite um valor valido!')

main()




""" livros = []
quantidade = []
emprestimos = []

def mensagem(msg):
    print(msg)

def cadastrar_livro(livro, qntd):
    livros.append(livro)
    quantidade.append(qntd)
    return mensagem('Livro(s) cadastrado(s)')

def mostrar_livros():
    for i in range(len(livros)):
        mensagem(f'{i+1} - {livros[i]} - und.{quantidade[i]}')

def fazer_pedido(emprestimo):
    emprestimos.append(emprestimo)

def calcular_total():
    return len(emprestimos)

def menu():
    print('==== Biblioteca ====')
    print('1- Cadastrar Livro 2 - Mostrar Livros 3- Fazer Emprestimo 4 - Mostrar Total 5 - Sair')


def main():
    while True:
        menu()
        opcao = int(input('Escolha uma opção: '))
        if opcao == 1:
            livro = input('Digite o livro a ser cadastrado: ')
            qntd = float(input('Informe a quantidade: '))
            cadastrar_livro(livro, qntd)
            mensagem('Livro Cadastrado com SUCESSO!')

        elif opcao == 2:
            mensagem('==== LIVROS ====')
            mostrar_livros()

        elif opcao == 3:
            mensagem('==== LIVROS ====')
            mostrar_livros()
            escolha = int(input('Escolha o livro pelo número: '))
            fazer_pedido(escolha)
            mensagem('Emprestimo Realizado')

        elif opcao == 4:
            mensagem(f'O total de livros emprestados é de {calcular_total()}')  

        elif opcao == 5:
            mensagem('Saindo...')
            break

        else:
            print('Digite um valor valido!')
              
main() """