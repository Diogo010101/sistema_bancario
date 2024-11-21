from time import sleep
import datetime


data = datetime.datetime.now()




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
numero_transacoes = 0
limite_transacoes = 5
transacoes = {}
numero_deposito = 0
data_transacao = ''


while True:

    opcao = str(input(menu))

    if opcao.upper() == 'D':
        deposito= int(input('Digite o valor que deseja depositar: '))
        if numero_transacoes >= limite_transacoes:
            print('Você atingio o limite de transações diárias!') 
        elif deposito > 0 and numero_transacoes <= limite_transacoes :
            if data_transacao == '':
                data_transacao = data.strftime('%d/%m/%Y')
                numero_transacoes += 1
            elif data_transacao == data.strftime('%d/%m/%Y') and numero_transacoes <= limite_transacoes:
                numero_transacoes += 1
            elif data_transacao != "" and data_transacao != data.strftime('%d/%m/%Y'):
                numero_transacoes = 0
            numero_deposito += 1
            saldo += deposito
            if numero_transacoes == 0:
                numero_transacoes = 1
            chave = f'Transação: {numero_transacoes}'
            data_atual = data.strftime("%d/%m/%Y %H:%M")
            valor = f"{data_atual}"
            transacoes.update({chave:valor})

            chave = f'Deposito: {numero_deposito}'
            valor = f"R$ {deposito:.2f} - Dia e Hora: {data_atual}\nSaldo após a transação: R${saldo:.2f}\n"
            extrato.update({chave:valor})
        else:
            print('O valor deve sar maior do que "0"')


    elif opcao.upper() == 'S':
        saque = int(input('Qual valor deseja sacar? [Limite de 500 por saque]>'))
        if numero_saque >= 3:
            print('Você atingiu o limite de saques diários')
        elif numero_transacoes >= limite_transacoes:
            print("Você atingiu o número máximo de transações diárias!")
        elif saque > 500:
            print('O valor máximo de saque por transação é do R$500')
        elif saque <= 0:
            print('Não é possível sacar um valor menor ou igual a 0')
        elif saque > 0 and saque <= 500 and numero_saque <=3 or transacoes <= limite_transacoes:
            if data_transacao == '':
                data_transacao = data.strftime('%d/%m/%Y')
                numero_transacoes += 1
            elif data_transacao == data.strftime('%d/%m/%Y') and numero_transacoes <= limite_transacoes:
                numero_transacoes += 1
            elif data_transacao != "" and data_transacao != data.strftime('%d/%m/%Y'):
                numero_transacoes = 0
            saldo -= saque
            numero_saque += 1
            if numero_transacoes == 0:
                numero_transacoes = 1
            print(f'''Saque de R$ {saque:.2f} realizado com sucesso!
                  Saldo atual R$ {saldo:.2f}''')
            chave = f'Transação: {numero_transacoes}'
            data_atual = data.strftime("%d/%m/%Y %H:%M")
            valor = f"{data_atual}"
            transacoes.update({chave:valor})

            chave = f'Saque: {numero_saque}'
            valor = f"R$ {deposito:.2f} - Dia e Hora: {data_atual}\nSaldo após a transação: R${saldo:.2f}\n"
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
numero_transacoes = 0
limite_transacoes = 5
transacoes = {}
numero_deposito = 0


while True:

    opcao = str(input(menu))

    if opcao.upper() == 'D':
        deposito= int(input('Digite o valor que deseja depositar: '))
        if deposito > 0 and numero_transacoes <= limite_transacoes:
            print(f'Realizando deposito de {deposito:.2f}')
            sleep(3)
            if data_transacao == '':
                data_transacao = data.strftime('%d/%m/%Y')
                numero_transacoes += 1
            elif data_transacao == data.strftime('%d/%m/%Y') and numero_transacoes <= limite_transacoes:
                numero_transacoes += 1
            elif data_transacao != "" and data_transacao != data.strftime('%d/%m/%Y'):
                numero_transacoes = 0
            numero_deposito += 1
            saldo += deposito
            if numero_transacoes == 0:
                numero_transacoes = 1

            chave = f'Transação: {numero_transacoes}'
            data_atual = data.strftime("%d/%m/%Y %H:%M")
            valor = f"{data_atual}"
            transacoes.update({chave:valor})

            chave = f'Deposito: {numero_deposito}'
            valor = f"R$ {deposito:.2f} - Dia e Hora: {data_atual}\nSaldo após a transação: R${saldo:.2f}\n"
            extrato.update({chave:valor})
            print(f'Depósito de R${deposito:.2f} realizado com sucesso!\nSaldo atualizado: R${saldo:.2f}')
            sleep(1)
        elif deposito < 0:
            print('O valor deve sar maior do que "0"')
            


        else:
            print("Você atingiu o limite de transações diárias")


    elif opcao.upper() == 'S':
        saque = int(input('Qual valor deseja sacar? [Limite de 500 por saque]>'))
        if numero_saque >= limite_saque:
            print('Você atingiu o limite de saques por dia')
        elif numero_transacoes >= limite_transacoes:
            print('Limite de transações diárias atingido')
        elif saque > 500:
            print('O valor máximo de saque por transação é do R$500')
        elif saque <= 0:
            print('Não é possível sacar um valor menor ou igual a 0')
        elif saque > 0 and saque <= 500 and numero_saque <=3 and numero_transacoes <= limite_transacoes:
            if data_transacao == '':
                data_transacao = data.strftime('%d/%m/%Y')
                numero_transacoes += 1
            elif data_transacao == data.strftime('%d/%m/%Y') and numero_transacoes <= limite_transacoes:
                numero_transacoes += 1
            elif data_transacao != "" and data_transacao != data.strftime('%d/%m/%Y'):
                numero_transacoes = 0
            saldo -= saque
            numero_saque += 1
            print(f'Realizando saque de {saque:.2f}')
            sleep(3)
            print(f'''Saque de R$ {saque:.2f} realizado com sucesso!
                  Saldo atual R$ {saldo:.2f}''')
            if numero_transacoes == 0:
                numero_transacoes = 1
            chave = f'Transação: {numero_transacoes}'
            data_atual = data.strftime("%d/%m/%Y %H:%M")
            valor = f"{data_atual}"
            transacoes.update({chave:valor})

            chave = f'Saque: {numero_saque}'
            valor = f"R$ {deposito:.2f} - Dia e Hora: {data_atual}\nSaldo após a transação: R${saldo:.2f}\n"
            extrato.update({chave:valor})
            sleep(1)

        else:
            print('Verifique os valores digitados')
        

    
    elif opcao.upper() == 'E':
        print(f'\n\n{'-'*5}EXTRATO BANCÁRIO{'-'*5}')
        print('IMPRIMINDO EXTRATO...')
        sleep(3)
        for key, value in extrato.items():
            print(key, '→', value)
        print(f'\n\nSaldo R${saldo:.2f}')

    elif opcao.upper() == 'Q':
        print('Encerrando sistema...')
        break

    else:

        print('Verifique a opção digitada e tente novamente.')



