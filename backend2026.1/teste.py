
class ContaBancaria:
    def __init__(self):
        self.saldo = 0
   
    def saldo_atual(self):
        print(f"Saldo atual: R${self.saldo:.2f}")
   
    def realizar_deposito(self):
        info_deposito =  int(input("Digite o valor do depósito: "))
        if info_deposito > 0:
            print(f"Depósito de R${info_deposito:.2f} realizado com sucesso.")    
        else:
            info_deposito == 0
            print("Valor de depósito inválido.")
        self.saldo += info_deposito

conta = ContaBancaria()
conta.saldo_atual()
conta.realizar_deposito()
conta.saldo_atual()