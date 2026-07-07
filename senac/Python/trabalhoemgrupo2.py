print(35*"-")
print("|Sistema de Compras Mercado Python|")
print(35*"-")
 
lista = [
    ("banana", 5.00), ("maçã", 2.00), ("leite", 4.50),
    ("refrigerante", 5.00), ("arroz", 10.00), ("feijão", 7.50),
    ("ovos", 15.00), ("pão", 6.00), ("café", 14.00), ("queijo", 11.00)
]
 
valor_total = 0
carrinho_qtd = 0
valore = []
 
print("AVISO: Na compra de 5 itens você ganha um desconto de 10% no valor da sua compra!")
print(30*"-")
print("1 - Banana - R$5,00")
print("2 - Maçã - R$2,00")
print("3 - Leite - R$4,50")
print("4 - Refrigerante - R$5,00")
print("5 - Arroz - R$10,00")
print("6 - Feijão - R$7,50")
print("7 - Ovos - R$15,00")
print("8 - Pão - R$6,00")
print("9 - Café - R$14,00")
print("10 - Queijo - R$11,00")
print(30*"-")
 
while True:
    entrada = input("Digite o número ou s para sair: ").lower()
    
    if entrada in ['sair' , 's', 'fechar', 'final', 'finalizar', 'sai']:
        break
 
    try:
        opcao = int(entrada)
 
        if opcao >= 1 and opcao <= 10:
            item = lista[opcao - 1]
            carrinho_qtd = carrinho_qtd + 1
            valor_total = valor_total + item[1]
            valore.append(item)

            print("Item adicionado com sucesso!")
            print(f'O item adicionado foi: {item[0]}')
        else:
            print("Número inválido! Escolha de 1 a 10.")
           
    except ValueError:
        print("Erro! Digite apenas o número do produto ou 's' para sair.")
 
valor_cheio = valor_total
valor_desconto = 0

if carrinho_qtd >= 5:
    valor_desconto = valor_cheio * 0.10
    valor_total = valor_cheio - valor_desconto

maiscaro = max(valore, key=lambda x: x[1]) 
 

print('\n' + '='*40)
print(f"{'NOTA FISCAL':^40}")
print('='*40)
print("Quantidade de itens:", carrinho_qtd)
print("Valor total: R$", valor_cheio)
print(f'O item mais caro é:{maiscaro}')
 
if valor_desconto > 0:
    print("Desconto aplicado (10%): R$", valor_desconto)
    print(30*"-")
    print("TOTAL A PAGAR: R$", valor_total)
else:
    print("TOTAL A PAGAR: R$", valor_total)
 
print('='*40)
print("Obrigado por comprar conosco!")