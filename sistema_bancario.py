def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print("Depósito realizado com sucesso.")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def sacar(saldo, limite, valor, extrato, numero_saques, LIMITE_SAQUES):
    if valor <= 0:
        print("Operação falhou! O valor informado é inválido.")
    elif valor > saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif valor > limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif numero_saques >= LIMITE_SAQUES:
        print("Operação falhou! Número máximo de saques excedido.")
    else:
        saldo -= valor
        extrato.append(f"Saque: R$ {valor:.2f}")
        numero_saques += 1
        print("Saque realizado com sucesso.")
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        for linha in extrato:
            print(linha)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def obter_valor(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Valor inválido. Por favor, digite um número.")

def main():
    MENU = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    => """
    SALDO_INICIAL = 0
    LIMITE_SAQUE = 500
    LIMITE_SAQUES_DIARIO = 3

    saldo = SALDO_INICIAL
    extrato = []
    numero_saques = 0

    while True:
        opcao = input(MENU).lower()

        if opcao == "d":
            valor = obter_valor("Informe o valor do depósito: ")
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = obter_valor("Informe o valor do saque: ")
            saldo, extrato, numero_saques = sacar(saldo, LIMITE_SAQUE, valor, extrato, numero_saques, LIMITE_SAQUES_DIARIO)

        elif opcao == "e":
            exibir_extrato(saldo, extrato)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()
