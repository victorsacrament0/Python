print("Digite as notas para saber a média: (De 0 a 10) \n")
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))
media = (nota1 + nota2 + nota3) / 3
print(f"A média das notas é: {media}")

if media >= 7:
    print("Média >= 7: Aprovado")
if media < 7:
    print("Média < 7: Reprovado")
