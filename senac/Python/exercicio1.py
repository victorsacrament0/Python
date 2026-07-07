print(f"Calculadora Basal Masculina (TBM) \n")
nome = input("Digite seu nome:")
idade = int(input("Digite sua idade:"))
altura = float(input("Digite sua altura(em cm):"))
peso = float(input("Digite seu peso: "))
calorias = (66 + (13.7 * peso) + (5 * altura) - (6.8 * idade))
print(f"Nome: {nome}" + '\n')
print("Idade: " + str(int(idade)) + '\n')
print("Altura: " + str(float(altura)) + "\n")
print(f"Peso: " + str(peso) + '\n')
print('Calorias Diarias:' + str(calorias))
print('(Referencia: Peso: {},altura: {},idade: {})'.format(peso, altura, idade))

"""Solicite ao usuário nome, idade e altura e exiba usando as quatro formas de print.
Converta idade para int e altura para float
Solicite dois números, some-os, e exiba o resultado usando todas as formas de concatenação. (fiz um pouco mais)"""
