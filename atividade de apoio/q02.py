'''
Crie um programa que cadastre informações de várias pessoas (nome, idade e cpf) e depois coloque em um dicionário. 
Depois remova todas as pessoas menores de 18 anos do dicionário e coloque em outro dicionário
'''

agenda = {}
menores18 = {}

def cadastrar():
    separar()
    cpf = int(input('informe o cpf: '))
    nome = input('informe o nome: ')
    idade = int(input('informe a idade: '))
    fone = int(input('informe o telefone: '))
    agenda[cpf] = [nome, idade, fone]
    separar()
    aux = input('voçe deseja adicionar outro usuario (s/n): \n')
    if aux == 's':
        cadastrar()
    elif aux != 'n':
        print('opição invalida')

def separar():
    print('========================================')

cadastrar()
aux = []
for i, j in agenda.items():
    if j[1] < 18:
        menores18[i] = [j[0], j[1], j[2]]
        aux.append(i)
for i in aux:
    agenda.pop(i)
separar()
print("\tUuarios:")
for i, j in agenda.items():
    print(f'{i}: {j[0]}-{j[1]}-{j[2]}')
separar()
print('menores de 18:')
for i, j in menores18.items():
    print(f'{i}: {j[0]}-{j[1]}-{j[2]}')

