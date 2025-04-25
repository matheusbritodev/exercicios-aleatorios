saldo = float(input('Digite o saldo incial:'))
while True:
    options = input('\nDigite o número de uma das opcões abaixo: \n1 - Ver saldo\n2 - Sacar\n3 - Depositar\n4 - Sair\n\n')
    if options == "1":
        print('Seu saldo é de: R${:.2f}'.format(saldo))
    elif options == "2":
        saque = float(input('Quanto você deseja sacar?'))
        if saldo > saque:
            saldo -= saque
            print('Saque realizado com sucesso!\nO seu saldo agora é de: R${:.2f}'.format(saldo))
        else:
            print('O seu saldo não é suficiente.')
    elif options == "3":
        deposito = float(input('Quanto você deseja depositar?'))
        saldo += deposito
        print('O seu saldo agora é de R${:.2f}'.format(saldo))
    elif options == "4":
        confirme = input('Você tem certeza que deseja sair do menu de opções? \n[Sim/Não]')
        if confirme.lower() in ["sim", "si", "s"]:
            break
        else: 
            continue
    else:
        print('Essa opção é inválida!')
