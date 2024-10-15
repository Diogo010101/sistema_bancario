menu = f'''\n{'-' *5}BANCO SAQUE MIL{'-' *5}

[D] Depósito
[S] Sacar
[E] Extrato
[Q] Sair

=>'''
saldo = 0
limite = 500
extrato = {}
numero_saque = 0
limite_saque = 3
numero_deposito = 0


while True:

    opcao = str(input(menu))

    if opcao.upper() == 'D':
        deposito= int(input('Digite o valor que deseja depositar: '))
        if deposito > 0:
            numero_deposito += 1
            saldo += deposito
            chave = f'Deposito: {numero_deposito}'
            valor = f"R$ {deposito:.2f}"
            extrato.update({chave:valor})
        else:
            print('O valor deve sar maior do que "0"')


    elif opcao.upper() == 'S':
        saque = int(input('Qual valor deseja sacar? [Limite de 500 por saque]>'))
        if numero_saque >= 3:
            print('Você atingiu o limite de saques por dia')
        elif saque > 500:
            print('O valor máximo de saque por transação é do R$500')
        elif saque <= 0:
            print('Não é possível sacar um valor menor ou igual a 0')
        elif saque > 0 and saque <= 500 and numero_saque <=3:
            saldo -= saque
            numero_saque += 1
            print(f'''Saque de R$ {saque:.2f} realizado com sucesso!
                  Saldo atual R$ {saldo:.2f}''')
            chave = f'Saque: {numero_saque}'
            valor = f"R$ {saque:.2f}"
            extrato.update({chave:valor})
        else:
            print('Verifique os valores digitados')
        

    
    elif opcao.upper() == 'E':
        print(f'\n\n{'-'*5}EXTRATO BANCÁRIO{'-'*5}')
        for key, value in extrato.items():
            print(key, '→', value)
        print(f'\n\nSaldo R${saldo:.2f}')

    elif opcao.upper() == 'Q':
        print('Encerrando sistema...')
        break

    else:
        print('Verifique a opção digitada e tente novamente.')