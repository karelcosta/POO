contas = []
ncontas = 0

def menu_inicial(nconta):
    print('\n\tMENU\n')
    op = None
    op = int(input(' 1- cadastrar conta\n 2- encontrar conta\n 3- fechar \nInforme a sua escolha: '))
    if op == 1:
        print('\n')
        nconta += 1
        contas.append(cadastrar(nconta))
        print('\nconta cadastrada com sucesso')
    elif op == 2:
        print('\n')
        encontrar_conta()
    elif op == 3:
        print('fechando . . .')
        return
    elif op == 999:
        mostrartodasascontas()
    else:
        print('\nopição invalida\n')
    menu_inicial(nconta)

def cadastrar(nconta):
    print(f'conta nº {nconta}')
    titular = input('informe o nome do titular da conta: ')
    saldo = float(input('informe o saldo da conta: '))
    usuario = {'numero': nconta, 'titular': titular,'saldo': saldo}
    return usuario


def encontrar_conta():
    n = int(input("informe o numero da conta: "))
    for i in contas:
        if i['numero'] == n:
            menu_conta(i)
            return
    print('\nconta não encontrada')

def menu_conta(conta):
    print('\n\tconta ', conta['numero'])
    print('\t', conta['titular'])
    print('1- Remover Conta\n2- Realizar transferência\n3- Exibir saldo\n4- Deposita Valor\n5- saque\n6- voltar')
    op = None
    op = int(input('informe a operação que deseja realizar: '))
    print('\n')
    if op == 1: #remoção
        contas.remove(conta)
        print('conta removida com suçesso')
        return
    elif op == 2:
        tranferencia1(conta)
    elif op == 3:
        print('\nsaldo da conta: ',  conta['saldo'])
    elif op == 4: #deposito
        valor = float(input('informe o valor que deseja depositar: '))
        conta['saldo'] += valor
        print('\nopreação finalizada com sucesso\n')
    elif op == 5: #saque
        valor = float(input('informe o valor que deseja sacar: '))
        if valor > conta['saldo']:
            print('\nsaldo insuficiente\n\nfinalizando operação')
        else:
            conta['saldo'] -= valor
            print('\nopreação finalizada com sucesso\n')
    elif op == 6: #voltar
        print('voltando para o nenu inicial')
        return
    else:
        print('opção invalida')
    menu_conta(conta)

def mostrartodasascontas():
    n = 0
    for i in contas:
        print(i)
        n += 1
    print(f'numero de contas: {n}')

def tranferencia1(conta):
    n = int(input("informe o numero da conta: "))
    for i in contas:
        if i['numero'] == n:
            tranferencia2(conta, i)
            return
    print('\nconta não encontrada\n')
    op = int(input('1- tentar novamente\n2- cancelar\nop:'))
    if op == 1:
        tranferencia1(conta)
    elif op == 2:
        return
    else: 
        print("opção invalida\ncancelando operação")
        return

def tranferencia2(conta, contaalvo):
    if conta == contaalvo:
        print('contas iguais') 
        op = int(input('1- tentar novamente\n2- cancelar\nop:'))
        if op == 1:
            tranferencia1(conta)
        elif op == 2:
            return
        else: 
            print("opção invalida\ncancelando operação")
        return
    else:
        tranferencia3(conta, contaalvo)

def tranferencia3(conta, contaalvo):
    valor = float(input('informe o valor da transferencia: '))
    if valor > conta['saldo']:
        print('saldo insuficiente\n')
        op = int(input('1- tentar novamente\n2- cancelar\nop:'))
        if op == 1:
            tranferencia3(conta, contaalvo)
        elif op == 2:
            return
        else: 
            print("opção invalida\ncancelando operação")
        return
    else: 
        conta['saldo'] -= valor
        contaalvo['saldo'] += valor

menu_inicial(ncontas)