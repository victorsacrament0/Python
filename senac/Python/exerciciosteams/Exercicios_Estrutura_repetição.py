# 1-Crie um programa que mostre todos os números pares entre dois números informados pelo usuário.

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

#2 Simule uma votação com 5 pessoas. Pergunte o voto (1,2 e 3) e mostre no final qual opção teve mais votos

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