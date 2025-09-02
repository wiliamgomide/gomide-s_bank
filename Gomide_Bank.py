menu = """
================ MENU ================
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
======================================
=> """

saldo = 0
limite_saque_valor = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES_DIARIOS = 3

while True:

    opcao = input(menu).lower()

    if opcao == "d":
        try:
            valor = float(input("Informe o valor do depósito: R$ "))

            if valor > 0:
                saldo += valor
                extrato += f"Depósito: R$ {valor:.2f}\n"
                print("\n=== Depósito realizado com sucesso! ===")
            else:
                print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
        except ValueError:
            print("\n@@@ Operação falhou! Por favor, insira um valor numérico. @@@")


    elif opcao == "s":
        try:
            valor = float(input("Informe o valor do saque: R$ "))

            excedeu_saldo = valor > saldo
            excedeu_limite_valor = valor > limite_saque_valor
            excedeu_limite_saques = numero_saques >= LIMITE_SAQUES_DIARIOS

            if excedeu_saldo:
                print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

            elif excedeu_limite_valor:
                print(f"\n@@@ Operação falhou! O valor do saque excede o limite de R$ {limite_saque_valor:.2f}. @@@")

            elif excedeu_limite_saques:
                print("\n@@@ Operação falhou! Número máximo de saques diários excedido. @@@")

            elif valor > 0:
                saldo -= valor
                extrato += f"Saque:    R$ {valor:.2f}\n"
                numero_saques += 1
                print("\n=== Saque realizado com sucesso! ===")

            else:
                print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
        except ValueError:
            print("\n@@@ Operação falhou! Por favor, insira um valor numérico. @@@")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo:    R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        print("\nObrigado por usar nosso sistema bancário. Até logo!")
        break

    else:
        print("\n@@@ Operação inválida, por favor selecione novamente a operação desejada. @@@")
