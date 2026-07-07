lista = []
 
while True:
    try:  
       print('_'*60 +'\n')
       print('        --- Bem-Vindo ao Mercado Python ---')
       print('    --- Digite o número referente a operação desejada ---\n')
       print('1-Adicionar | 2-Remover | 3-Listar | 4-Ver Carrinho/Total | 5-Sair/Finalizar \n')
       
       prod = int(input('Digite a opção desejada: '))
       print('_'*60 +'\n')
 
       if prod < 1 or prod > 5:
           print('Valor Inválido!\n')
           continue  
 
       if prod == 1:
           nome = input('Digite o nome do produto: ').lower()
           preco = float(input(f'Digite o preço de "{nome}": '))
           produto = (nome, preco)
           lista.append(produto)
           print(f'"{nome}" adicionado com sucesso!')
 
       elif prod == 2:
           rem = input('Digite o nome exato do produto para remover: ').lower()
           encontrado = False
           for p in lista:
               if p[0] == rem:
                   lista.remove(p)
                   print(f'"{rem}" removido!')
                   encontrado = True
                   break
           if not encontrado:
               print("Produto não encontrado.")
 
       elif prod == 3:
           print("--- Itens no Carrinho ---")
           for p in sorted(lista):
               print(f"- {p[0]}: R$ {p[1]:.2f}")
 
       elif prod == 4:
          quantidade = len(lista)
          total = sum(p[1] for p in lista)
          print(f'Quantidade de itens: {quantidade}')
          print(f'Valor atual: R$ {total:.2f}')
 
       elif prod == 5:
           break
 
    except ValueError:
        print('_' * 60)
        print('Erro! Digite um valor numérico válido.')
 
if lista:
    total_final = sum(p[1] for p in lista)
    qtd_final = len(lista)
    
    mais_caro = max(lista, key=lambda x: x[1])
    
    desconto = 0
    if total_final > 100:
        desconto = total_final * 0.10
    
    print('\n' + '='*40)
    print(f"{'NOTA FISCAL':^40}")
    print('='*40)
    for p in lista:
        print(f"{p[0].capitalize():.<30} R$ {p[1]:>7.2f}")
    
    print('-'*40)
    print(f"Subtotal: {' '*18} R$ {total_final:>7.2f}")
    if desconto > 0:
        print(f"Desconto (10%): {' '*12} -R$ {desconto:>7.2f}")
        print(f"TOTAL FINAL: {' '*15} R$ {total_final - desconto:>7.2f}")
    
    print(f"\nQuantidade de itens: {qtd_final}")
    print(f"Produto mais caro: {mais_caro[0]} (R$ {mais_caro[1]:.2f})")
    print('='*40)
else:
    print("\nCarrinho vazio. Nenhuma compra realizada.")
 
print('Obrigado por nos escolher! Volte Sempre!')
print('_' * 60 , '\n')
    
#key=lambda: Define qual atributo do objeto deve ser usado para ordenar.
#lambda x: x[1]: Uma função anônima (lambda) que pega um item x e retorna o seu segundo elemento (x[1])
"""
produtos = [("Camisa", 50), ("Calça", 120), ("Sapato", 80)]

# max() vai olhar para o x[1] (preço) de cada tupla
mais_caro = max(produtos, key=lambda x: x[1])

print(mais_caro)
# Resultado: ('Calça', 120)
"""