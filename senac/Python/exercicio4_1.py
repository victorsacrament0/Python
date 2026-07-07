
idade = int(input("Digite sua idade: "))
tem_carteira = input("Você tem carteira de motorista? (sim/nao): ")
if idade >= 18 and tem_carteira == "sim":
    print("Você pode dirigir.")
if idade >= 18 and tem_carteira == "nao":
    print("Você não pode dirigir.")
if idade <= 17 and tem_carteira == "nao":
    print("Você não pode dirigir.")
else:
    print("Você não pode dirigir.")