cinema = []
ingressos_vendidos = []
valores_arrecadados = []

def mensagem(msg):
    print(msg)

def cadastro_filmes():
    nome_filme = input('Nome do filme: ')
    cinema.append(nome_filme)
    mensagem('Filme Cadastrado!')

def mostrar_filmes():
    mensagem('\n==== FILMES ====')
    for i in range(len(cinema)):
        mensagem(f'{i+1} - {cinema[i]}')


def registrar_venda():
    
    filme = input("Digite o nome do filme: ")
    try:
        quantidade = int(input("Quantidade de ingressos: "))
        preco = float(input("Preço unitário do ingresso (R$): "))
        
        if quantidade > 0 and preco >= 0:
            total_venda = quantidade * preco
            ingressos_vendidos.append(quantidade)
            valores_arrecadados.append(total_venda)
            print('_'*35)
            print(f"\n{quantidade} ingresso(s) registrado(s) com sucesso! Total da venda: R$ {total_venda:.2f}")
        else:
            print("\nQuantidade e preço devem ser valores positivos.")
    except ValueError:
        print("\nEntrada inválida. Digite apenas números.")
        print('_'*35,'\n')

    
    print(f'O filme escolhido foi {filme}, \nPreço unitário: R${preco:.2f}, \nQaunditade: {quantidade}')

def calcular_total_arrecadado():
    total = sum(valores_arrecadados)
    return total

def mostrar_quantidade_vendida():
    total_ingressos = sum(ingressos_vendidos)
    return total_ingressos

def main():
    while True:
        print("\n" + "="*30)
        print("   SISTEMA DE BILHETERIA")
        print("="*30)
        print("1 - Registrar Venda")
        print("2 - Mostrar Valor Arrecadado")
        print("3 - Mostrar Quantidade de Ingressos Vendidos")
        print("4 - Cadastrar Filmes")
        print("5 - Mostrar Filmes")
        print("6 - Sair")
        
        opcao = input("Escolha uma opção (1-6): ")
        
        if opcao == "1":
            mostrar_filmes()
            registrar_venda()
        elif opcao == "2":
            total = calcular_total_arrecadado()
            print(f"\nValor total arrecadado: R$ {total:.2f}")
        elif opcao == "3":
            quantidade = mostrar_quantidade_vendida()
            print(f"\nTotal de ingressos vendidos: {quantidade} unidade(s)")
        elif opcao == "4":
            cadastro_filmes()
        elif opcao == "5":
            mostrar_filmes() 
        elif opcao == "6":
            print("\nSaindo. Até logo!")
            break
        else:
            print("\nOpção inválida! Tente novamente.")


main()


