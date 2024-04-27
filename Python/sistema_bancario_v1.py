"""
Seguindo a base dado pelo professor com algumas poucas alterações para reducao de linhas
e aprimiracao de conceitos.
"""

SAQUE_LIMITE, QTD_SAQUES = 500, 3
saldo, numero_saques = 0, 0
extrato = ""

while True:
    opcao = input("\n[d] Depositar \n[s] Sacar \n[e] Extrato \n[f] Finalizar \n\n=> ").lower()
    
    if opcao == "f":
        break
    elif opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        if valor > saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif valor > SAQUE_LIMITE:
            print("Operação falhou! O valor do saque excede o limite.")
        elif numero_saques >= QTD_SAQUES:
            print("Operação falhou! Número máximo de saques excedido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
