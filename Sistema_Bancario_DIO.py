menu = """

########## Bem vindo ao Banco Sieg!##########

Digite o número da operação que deseja fazer!

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        print(" ## Bem vindo a pagina de Depósito! (Não aceitamos valores negativos!) ## \n")
        valor = float(input("Informe o Valor do Depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é negativo!.")

    elif opcao == "2":
        print(f"Você possui R$ {saldo:.2f} em conta, quanto deseja sacar?\n Lembrando que o limite maximo de saque é de R$ 500! \n E você pode sacar apenas 3 vezes ao dia \n Você já sacou {numero_saques} hoje! \n") 
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else: 
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "3":
            print("\n================ EXTRATO ================")
            print("Não foram realizadas movimentações." if not extrato else extrato)
            print(f"\nSaldo: R$ {saldo:.2f}")
            print("==========================================")

    elif opcao == "4":
        print("==============================================")
        print("Obrigado por usar o nosso banco! Volte sempre!")
        print("==============================================")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")