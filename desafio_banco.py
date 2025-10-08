menu = """
    [D] = Depositar
    [S] = Sacar
    [E] = Extrato
    [Q] = Sair

=>""" 

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3


while True:

    opcao = input(menu)

    if opcao == "D" or opcao == "d":
        valor = float(input("Informe o valor a ser depositado: "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou!!!")
            print("O valor informado é inválido.")
        
    elif opcao == "S" or opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= limite_saques

        if excedeu_saldo:
            print("Operação falhou!")
            print("Você nao tem saldo suficiente!!!")
        
        elif excedeu_limite:
            print("Operação falhou!")
            print("Você nao tem limite suficiente!!!")
        elif excedeu_saques:
            print("Operação falhou!")
            print("Você já realizou mais de {excedeu_saques} saques!!!")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Operação falhou!")
            print("O valor informado é inválido!!!")
        

    elif opcao == "E" or opcao == "e":
        print("\n=============EXTRATO BANCARIO=================")
        print("Não foram realizadas movimentações" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===============EXTRATO BANCARIO=================")

    
    elif opcao == "Q" or opcao == "q":
        break

    else:
        print("Opção invalida!!!")
        print("Selecione novamente uma opção!!!! ")

