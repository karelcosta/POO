funcionarios = []
aux = True

def separar():
    print('\n------------\n')

def cadastrar_funcionario():
    nome = input('informe o nome do funcionario: ')
    cpf = int(input('informe o cpf do funcionario: '))
    cargo = input('informe o cargo do funcionario: ')
    salario = float(input('informe o salario do funcionario: '))
    telefone = []
    telefone.append(int(input('informe o telefone do funcionario: ')))
    funcionario = {'nome': nome, 'cpf': cpf, 'cargo': cargo, 'salario': salario, 'telefones': telefone}
    return funcionario

def encontrar():
    n = (input("informe o cpf do funcionario da conta: "))
    for i in funcionarios:
        if i['cpf'] == n:
            return i
    print('\nfuncionario não encontrado')
    return -1

def menu1(aux):
    separar()
    print('\tMENU\n\n')
    op = None
    print(' 1- cadastrar funcionario\n 2- encontrar funcionario\n 3- cadastrar novo telefone \n 4- editar dados do funcionario  ')
    op = int(input(' 5- deletar funcionario\n 0- sair\nop:'))
    if op == 1:
        separar()
        funcionarios.append(cadastrar_funcionario())
        separar()
        print('funcionario cadastrado com sucesso')
        aux = True
    elif op == 2:
        separar()
        if aux:
            f = None
            f = encontrar()
            if f != -1:
                separar()
                exibirdados(f)
        else:
            print('não exixtem funcionarios')
    elif op == 3:
        separar()
        if aux:
            cadastrartelefone()
        else:
            print('não exixtem funcionarios')    
    elif op == 4:
        separar()
        if aux:
            f = None
            f = encontrar()
            editar(f)
        else:
            print('não exixtem funcionarios')
    elif op == 5:
        separar()
        if aux:
            f = None
            f = encontrar()
            if f != -1:
               funcionarios.remove(f)
               separar()
               print('funcionario removido com sucesso')
            aux2 = len(funcionarios)
            if aux2 == 0:
                aux = False
        else:
            print('não exixtem funcionarios')
    elif op == 0:
        separar()
        print('Saindo')
        separar()
        return
    else: 
        separar()
        print('opição invalida')
    menu1(aux)

def exibirdados(f):
    print('nome : ', f['nome'])
    print('cpf: ', f['cpf'])
    print('cargo: ', f['cargo'])
    print('salario: ', f['salario'])
    print('telefones: \n')
    for i in f['telefones']:
        print(i)

def cadastrartelefone():
    f = encontrar()
    if f != -1:
            f['telefones'].append(int(input('informe o novo numero: ')))
            separar()
            print('numero cadastrado com sucesso')

def editar(f):
    separar()
    print('\teditar\n')
    print('1- nome: ', f['nome'])
    print('2- cpf: ', f['cpf'])
    print('3- cargo: ', f['cargo'])
    print('4- salario: ', f['salario'])
    print('5- telefones: \n', f['telefones'])
    op = int(input('informe qual dado voce deseja alterar: '))
    separar()
    if op == 1:
        nvnome = input('informe o novo nome: ')
        f['nome'] = nvnome
        repetir(f)
    elif op == 2:
        nvcpf = input('informe o novo cpf: ')
        f['cpf'] = nvcpf
        repetir(f)
    elif op == 3:
        nvcargo = input('informe o novo cargo: ')
        f['cargo'] = nvcargo
        repetir(f)
    elif op == 4:
        nvsalario = input('informe o novo salario: ')
        f['salario'] = nvsalario
        repetir(f)
    elif op == 5:
        editarnumero(f)
        repetir(f)
    else: 
        print("opição invalida")
        print("\ndeseja tentar novamente?")
        opin = None
        opin = int(input('1- sim\n2- não'))
        if opin == 1:
            editar(f)
        elif opin == 2:
            print("voltando")
        else:
            print('opição invalida\nvoltando')

def repetir(f):
    separar()
    print("você deseja fazer mais alguma alteração?")
    opre = None
    opre = int(input('1- sim\n2- não\nop: '))
    if opre == 1:
        editar(f)
    elif opre == 2:
        print("\nvoltando")
        return 
    else:
        print('\nopição invalida\nvoltando')
        return

def editarnumero(f):
    print("informe qual numero deseja remover\n")
    j = 0
    for i in f['telefones']:
        j+=1
        print(f'[{j}] {i}')
    oprn = int(input('\nop:'))
    oprn -= 1
    f['telefones'].pop (oprn)
    separar()
    print("numero removido com sucesso")

menu1(aux)
