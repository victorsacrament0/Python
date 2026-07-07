print(('_' * 40 ) + '\n')
print("Bem-vindo ao Banco Python!")
print(('_' * 40 ) + '\n')

nome_titular = input("Informe o  nome da conta do titular: ")

print(('_' * 40 ) + '\n')
print(f"Conta aberta para {nome_titular}!")
print(('_' * 40 ) + '\n')

try:
            deposito_inicial = float(input("Digite o valor de depósito inicial: "))

            if deposito_inicial > 0:
                saldo = deposito_inicial
                print(40*("_"))
                print(f"\nSRº {nome_titular}, valor depositado com sucesso!")
                print(f"Saldo atual: R$ {saldo:.2f}")
            elif deposito_inicial == 0:
                saldo = deposito_inicial
                print(40*("_"))
                print("\n Valor inicial inválido. A conta não pode ser aberta com saldo R$ 0.00")
                print(40*("_"))
                
                print(40*("_"))
                print("Valor inválido! Digite um numero positivo para o depósito inicial.")
                print(40*("_"))
                
except ValueError:
            print(40*("_"))
            print("Operação inválida! Por favor, tente novamente.")
            print(40*("_"))
            

while True:   
    try: 
            v = input( f"SR {nome_titular} deseja relaizar alguma operação? (sim ou não)\n ").lower()

            if v in ["sim", "s", "si"]:
                print("Qual operação o Sr. gostaria de realizar? ")
                operacao = input("Opções [Sacar], [Depositar], [Saldo] , [Sair]: ").lower()
            elif v in ["não", "n", "nao"]:
                    print(40*("_"))
                    print("Atendimento encerrado!")
                    print(40*("_"))
                    break
            else:
                print(40*("_"))
                print("Resposta inválida! Por favor, responda com 'sim' ou 'não'.")
                print(40*("_"))
                continue
    
            if operacao in ['sair','sai','fecha','fechar']:
                 break
                    
            if operacao == "sacar":
                        
                valor_saque = float(input("Informe o valor do saque: R$ "))
                        
                if valor_saque <= saldo:
                    saldo -= valor_saque
                    print(40*("_"))    
                    print(f"Saque realizado!\n Valor sacado: R${valor_saque} \n Saldo atual: R$ {saldo:.2f}")
                    print(40*("_"))
                    continue
                if valor_saque > saldo:
                    print(40*("_"))
                    print("Erro: Saldo insuficiente para esta operação.")
                    print(40*("_"))
                    continue
                            
            elif operacao == "depositar":

                valor_depo = float(input("Informe o valor do depósito: R$ "))

                        
                if valor_depo > 0:
                    saldo += valor_depo  
                    print(40*("_"))
                    print(f"Depósito realizado!\n Valor depositado R${valor_depo} \n Saldo atual: R$ {saldo:.2f}")
                    print(40*("_"))
                    continue
                else:
                    print(40*("_"))
                    print("Erro: O valor do depósito deve ser maior que zero.")
                    print(40*("_"))
                    continue
                    
            elif operacao == "saldo":
                print(40*("_"))
                print(f"O seu saldo disponível é: R$ {saldo:.2f}")
                print(40*("_"))
                continue

            else:
                print(40*("_"))
                print("Atendiemnto encerrado!")
                print(40*("_"))
                continue

    except ValueError:
        print(40*("_"))
        print("Operação inválida! Por favor, tente novamente.")
        print(40*("_"))
        continue