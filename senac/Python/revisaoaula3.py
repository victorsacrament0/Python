#REVISAO AULA 3 - VARIÁVEIS E TIPOS DE DADOS
# nome idade cidade
name = "Victor"
age = 40
city = "Rio de Janeiro"
print("Meu nome é " + name + ", tenho " + str(age) + " anos e moro em " + city + ".")

#Crie duas variáveis numéricas, a e b.
#Some, subtraia, multiplique e divida essas variáveis.
#Exiba o resultado de cada operação.
#Dica: Use print("Soma:", a + b), etc.

a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))

print("Soma:", a + b)
print("Subtração:", (a - b))
print("Multiplicação:", a * b)
print("Divisão:", a / b)
print("Divisão Inteira:", a // b)
print("Resto da Divisão:", a % b)
print("Exponenciação:", a ** b)

#Crie uma variável saldo com valor inicial de 1000.
#Adicione 250 ao saldo.
#Subtraia 150 do saldo.
#Exiba o valor final do saldo.

saldo = 1000
saldo += 250
saldo -= 150    
print(f"Saldo final: {saldo}")    

#modo mais longo
#saldo = 1000
#saldo = saldo + 250
#saldo = saldo - 150
#print(f"Saldo Final: {saldo}")

print(30*'-')
print('|Bem Vindo ao Banco Python|')
print(30*'-')
saldo = 1000    
print(f"Saldo Atual: {saldo}")
deposito = float(input("Digite o valor do depósito: "))
saldo += deposito #saldo = saldo + deposito (modo mais longo)

print("O valor do deposito foi de {} e o Saldo após depósito: {}") .format (deposito,saldo)
saque = float(input("Digite o valor do saque: "))
saldo -= saque #saldo = saldo - saque (modo mais longo)
print("O valor do saque foi de {} e o Saldo após saque: {}") .format (saque,saldo)  
