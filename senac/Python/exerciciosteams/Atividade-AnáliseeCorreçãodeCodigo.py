# Solicitar o nome do cliente


nome_titular = input("Informe o  nome da conta do titular: ")

# Abertura da conta(Deposito inicial)

try:

    deposito_inicial = float(input("Digite o valor de depósito inicial: "))
# Validar se é numero
# if deposito_inicial.replace(".","",1).isdigit():
# deposito_inicial = float(deposito_inicial)

    # Valida se é maior que 0
    if deposito_inicial > 0:
        saldo = deposito_inicial
        print(f"\nSRº {nome_titular}, conta aberta com sucesso!")
        print(f"Saldo atual: R$ {saldo:.2f}")
    elif deposito_inicial == 0:
        saldo = deposito_inicial
        print("\nValor inicial inválido. A conta não pode ser aberta com saldo R$ 0.00")
        print(30*("-"))
        exit()
    else:
        print("Valor inválido! Digite um numero positivo para o depósito inicial.")
        print(30*("-"))
        exit()

# else:
# print("Valor inválido! Digite um numero") """

# 2. Pergunta de Operação
    verifica = input(f"SR {nome_titular} deseja relaizar alguma operação? (sim ou não) ").lower()

# if verifica == "sim": """
    if verifica in ["sim", "s", "si"]:
        print("Qual operação o Sr. gostaria de realizar? ")
        operacao = input("Opções [Sacar], [Depositar], [Saldo] ").lower()
    elif verifica in ["não", "n", "nao"]:
        print(40*("-"))
        print("Atendimento encerrado!")
        print(40*("-"))
        exit()
    else:
        print(40*("-"))
        print("Resposta inválida! Por favor, responda com 'sim' ou 'não'.")
        print(40*("-"))
        exit()

    # Estrutura de Decisão para Operações
    if operacao == "sacar":
        valor_saque = float(input("Informe o valor do saque: R$ "))
        # Verificação de Saldo Insuficiente
        if valor_saque <= saldo:
            saldo -= valor_saque
        print(f"Saque realizado! Saldo atual: R$ {saldo:.2f}")
        if valor_saque > saldo:
            print("Erro: Saldo insuficiente para esta operação.")
    elif operacao == "depositar":
        valor_depo = float(input("Informe o valor do depósito: R$ "))

        # Validação de Depósito Positivo
        if valor_depo > 0:
            saldo += valor_depo  # Aqui usamos o sinal de +
            print(f"Depósito realizado! Saldo atual: R$ {saldo:.2f}")
        else:
            print("Erro: O valor do depósito deve ser maior que zero.")
    elif operacao == "saldo":
        print(f"O seu saldo disponível é: R$ {saldo:.2f}")

    else:
        print("Atendiemnto encerrado!")

    print("-" * 30)

except ValueError:
    print("Operação inválida! Por favor, tente novamente.")


# Algumas identações estavam erradas e corrigi elas
# Algumas variáveis estavam com nomes diferentes e corrigi elas
# .2f = indica que o número deve ser exibido com 2 casas decimais
# .isdigit() = é um método de string em Python que verifica se todos os caracteres da string são dígitos (números).
#             Ele retorna True se a string contiver apenas dígitos e False caso contrário.
# uso do try - except para tratamento de erros, nesse caso, para garantir que o usuário digite um número válido
#              para o depósito inicial e para as operações de saque e depósito.
# .isdigit() retorna false para numeros float, por isso usei o try - except para validar se o valor digitado é um número
# adicionado o in[] para validação da resposta na linha 33
# adicionado o exit() para encerrar o programa caso o depósito inicial seja 0 ou negativo
