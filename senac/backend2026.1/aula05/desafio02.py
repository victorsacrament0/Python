class ContaBancaria:
    def __init__(self):
        self.__saldo = 0
   
    def saldo_atual(self):
        print(f"Saldo atual: R${self.__saldo:.2f}")
   
    def realizar_deposito(self):
        info_deposito =  int(input("Digite o valor do depósito: "))
        if info_deposito > 0:
            print(f"Depósito de R${info_deposito:.2f} realizado com sucesso.")    
        else:
            info_deposito == 0
            print("Valor de depósito inválido.")
        self.__saldo += info_deposito

conta = ContaBancaria()
conta.saldo_atual()
conta.realizar_deposito()
conta.saldo_atual()




""" terceira ideia

class ContaBancaria:
    def __init__(self):
        self.saldo =  0        
 
    def total_saldo(self):
        mensagem = f"O saldo atual é de R$ {self.saldo}"
        return mensagem
   
    def sobre_deposito(self):
        valor = int(input("Informe o valor a depositar: R$"))
 
        if valor > 0:
            self.saldo += valor
            print(f"Deposito de R${valor:.2f} foi feito")  
        else:
            print("Não foi possivel fazer esse depósito")
 
cliente = ContaBancaria()
 
print(f"Antes do deposito {cliente.total_saldo()}")
cliente.sobre_deposito()
 
print(cliente.total_saldo())

 """