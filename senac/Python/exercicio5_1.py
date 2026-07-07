print("Digite as notas para saber a média: (De 0 a 10) \n")
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))
media = (nota1 + nota2 + nota3) / 3
print(f"A média das notas é: {media}")

# sem if
print("Aprovado", media >= 5)
print("Reprovado", media < 5)

#mais curto ainda só com True ou False
resultado = media >= 5
print("Aprovado?", resultado)

# com if
if media >= 5:
    print("Aprovado!")
if media < 5:
    print("Reprovado!")
