'''
Crie um dicionário que é uma agenda e coloque nele os seguintes dados: chave (cpf), nome, idade, telefone. 
O programa deve ler um número indeterminado de dados, criar a agenda e imprimir todos os itens do dicionário no formato chave: 
nome-idade-fone
'''

agenda = {}

def cadastrar():
    separar()
    cpf = input('informe o cpf: ')
    nome = input('informe o nome: ')
    idade = int(input('informe a idade: '))
    fone = int(input('informe o telefone: '))
    agenda[cpf] = {'nome': nome, 'idade': idade, 'telefone': fone}
    separar()
    aux = input('voçe deseja adicionar outro usuario (s/n): \n')
    if aux == 's':
        cadastrar()
    elif aux != 'n':
        print('opição invalida')

def separar():
    print('========================================')

def menu():
    separar()
    print('################ M E N U ###############')
    separar()
    print("[1] - cadastrar usuario")
    print('[2] - visualisar')
    print('[3] - sair')
    separar()
    op = input('')
    if op == '1':
        cadastrar()
    elif op == '2':
        separar()
        print("\tUuarios:")
        for i, j in agenda.items():
            print(f'{i}: {j}')
    elif op == '3':
        separar()
        print('saindo . . .')
        return
    else:
        separar()
        print('opição invalida')
    menu()

menu()
