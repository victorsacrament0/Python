num1 = input('Digite um número')
num2 = input('Digite outro número')
def soma(num1,num2):
    """ resultado = num1 + num2
    print(resultado) """
    return num1 + num2

print(soma(num1,num2))

""" ============ """

num1 = input('Digite um número: ')
num2 = input('Digite outro número: ')
om = input('Digite um operador matematico: ')
def mult(num1,num2):
  return num1 * num2

print(mult(num1,num2))

""" =========== """
def desconto_10(valor_compra):
    #Calcula qunto é 10% do valor da compra
    desconto = valor_compra * 0.10
    return valor_compra - desconto
 
valor = int(input("Informe o valaor da compra: "))
print("Aplicando cupom de 10%. Aguarde.. ")
valor_desconto = desconto_10(valor)
 
print(f"Desconto aplicado! Valor a pagar R${valor_desconto:.2f}")

""" ========= """

def media (n1,n2):
   return (n1+n2) / 2

resultado = media(7,8)

print(resultado)