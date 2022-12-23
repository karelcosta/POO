from Class import *
import os

def menuIni():
   os.system('clear')
   print("==============MENU==============")
   print("1.Manter Funções\n2.Manter de Funcionários\n0.Sair")
   print("================================")
    
  
def menufunc():
   os.system('clear')
   print("1.Cadastrar Função\n2.Pesquisar Função\n3.Editar Função\n4.Deletar Função\n0.Voltar ao Menu Principal")
   print("================================")
   try:
      aux = int(input("Escolha uma opção: "))
   except:
      print('opição invalida')
      separar()
      menufunc()
   if aux == 1:
      try:
         Funcao(input("Digite o codigo da função: "), input("Digite o nome da função: "))
         connection.commit()
         print("Função cadastrada com sucesso!\n")
      except:
         print('ERRO: codigo ja em uso')
      # aux == 0
   elif aux == 2:
      if verificar_funcoes() == 0:
         separar()
         print('voçe não possue funções')
      else: 
         search_func()
      # aux = 0
   elif aux == 3:
      if verificar_funcoes() == 0:
         separar()
         print('voçe não possue funções')
      else: 
         print("O que deseja alterar?\n1-Codigo da função\n2-Nome da função\n3-Função inteira\n0-Voltar")
         try:
            aux2 = int(input('Escolha uma opção: '))
         except:
            print('opição invalida')
            separar()
            menufunc()
         if aux2 == 1:
            mudarcod_func()
         elif aux2 == 2:
            mudarnome_func()
         elif aux2 == 3:
            mudarcod_func()
            mudarnome_func()
   elif aux == 4:
      if verificar_funcoes() == 0:
         separar()
         print('voçe não possue funções')
      else: 
         delete_func()     
   elif aux == 0:
      pass
   else:
      print('opção invalida')
     

def menufuncionario():
   os.system('clear')
   print("1.Cadastrar Funcionário\n2.Pesquisar Funcionário\n3.Editar Funcionário\n4.Deletar Funcionário\n0.Voltar ao Menu Principal\n")
   print("================================")
   try:
      aux = int(input("Escolha uma opção: "))
   except:
      print('opição invalida')
      separar()
      menufuncionario()
   if aux == 1:
      if verificar_funcoes() == 0:
         separar()
         print('voçe não possue funções')
      else: 
         cad_funcionario()
   elif aux == 2:
      if verificar_funcionarios() == 0:  
         print('você não possue funcionarios')
      else:
         pesq_funcionario()
   elif aux == 3:
      if verificar_funcionarios() == 0:  
         print('você não possue funcionarios')
      else: 
         while aux3 != -1:
            try:
               aux3 = int(input("O que deseja alterar?\n1-Identidade\n2-Função\n3-Salario\n4-Telefone\n0-Voltar ao menu\nDigite sua escolha: "))
            except:
               print('opição invalida')
               separar()
               menufuncionario
            if aux3 == 1:
               alterID_funcionario()
               print("Funcionario alterado com sucesso!\n")
            elif aux3 == 2:
               alterFunc_funcionario()
               print("Funcionario movido com sucesso!\n")
            elif aux3 == 3:
               alterSAL_funcionario()
               print("Salario atualizado!\n")
            elif aux3 == 4:
               alterTEL_funcionario()
               print("Telefone alterado com sucesso!\n")
            elif aux3 == 0:
               aux3 = -1
               menufuncionario()
            
   elif aux == 4:
      if verificar_funcionarios() == 0:  
         print('você não possue funcionarios')
      else: 
         delete_funcionario()
   elif aux == 0:
      pass
   else:
      print('opção invalida')


def mudarcod_func():
   with connection.cursor() as c:
      sql = "UPDATE funcao SET cod = %s WHERE cod = %s"
      c.execute(sql,(input("Digite o novo Codigo da função: "), input("Digite o antigo Codigo da função: ") ))
      print("Alteração conculida!\n")
   connection.commit()
def mudarnome_func():
   with connection.cursor() as c:
      sql = "UPDATE funcao SET nome = %s WHERE nome = %s"
      c.execute(sql,(input("Digite o novo Nome da função: "), input("Digite o antigo Nome da função: ") ))
      print("Alteração conculida!\n")
   connection.commit()
def delete_func():
   try:
      with connection.cursor() as c:
         sql = "DELETE FROM funcao WHERE cod = %s"
         c.execute(sql, (input("Digite o codigo da função a ser deletada: ")))
         print("Função deletada com sucesso!\n")
      connection.commit()
   except:
      print('ERRO: você não pode deletar uma função que esteja em uso')
def search_func():
  with connection.cursor() as c:
      sql = "SELECT * FROM funcao WHERE cod = %s"
      c.execute(sql,(input("Digite o codigo da função: ")))
      Func = c.fetchone()
      print(Func)
def cad_funcionario():
   try:   
      nome = input("Digite o nome do funcionario:")
      while True:
         cpf = input("Digite o CPF do funcionario: (11: caracteres)\n")
         if len(cpf) != 11:
            print('cpf invalido\nnumero de caracteres invalido')
         else:
            break
      Funcionario(nome, cpf, input("Digite o codigo da função do funcionrio: "), float(input("Digite o salario do novo funionario: ")), input("Digite o telefone do funconario: ") )
      print("Cadastro feito com sucesso!\n")
   except:
      print('Erro no cadastro')
def pesq_funcionario():
   if verificar_funcionarios() == 0:  
      print('você não possue funcionarios')
   else: 
      with connection.cursor() as c:
         sql = "SELECT * FROM funcionario WHERE CPF = %s"
         c.execute(sql, (input("Digite o CPF do funcionario a ser procurado: ")))
         funcio = c.fetchone()
         print(funcio)

def alterID_funcionario():
   with connection.cursor() as c:
      sql = "UPDATE funcionario SET nome = %s WHERE nome = %s;\n UPDATE funcionario SET CPF = %s WHERE nome = %s"
      funcio = input("Digite o nome do funcionario a ser mudado: ")
      c.execute(sql,(input("Digite o novo nome do funcionario: "),funcio, input("Digite o novo CPF do funcionario"), funcio))
   connection.commit()
def alterFunc_funcionario():
   with connection.cursor() as c:
      sql = "UPDATE funcionario SET funcao = (SELECT id FROM funcao WHERE cod = %s) WHERE nome = %s"
      fucn = input("Digite o nome do funcionario que irá trocar de função: ")
      c.execute(sql, (input("Digiet o codigo da nova função do funcionario: "), fucn))
   connection.commit()
def alterSAL_funcionario():
   with connection.cursor() as c:
      sql = "UPDATE funcionario SET salario =  %s WHERE nome = %s"
      fucn = input("Digite o nome do funcionario que irá mudar o salario: ")
      c.execute(sql, (float(input("Digiet o novo salario do funcionario: ")), fucn))
   connection.commit()
def alterTEL_funcionario():
   with connection.cursor() as c:
      sql = "UPDATE funcionario SET telefone =  %s WHERE nome = %s"
      fucn = input("Digite o nome do funcionario que irá mudar o telefone: ")
      c.execute(sql, (input("Digiet o novo telefone do funcionario: "), fucn))
   connection.commit()
def delete_funcionario():
   with connection.cursor() as c:
      sql = "DELETE FROM funcionario WHERE nome = %s"
      c.execute(sql, (input("Digite o nome do funcionario a ser deletado: ")))
      print("Funcionario deletado com sucesso!\n")
   connection.commit()

def verificar_funcoes():
   with connection.cursor() as c:
      sql = "SELECT * from funcao"
      c.execute(sql)
      funcaoex = len(c.fetchall())
      return funcaoex
def verificar_funcionarios():
   with connection.cursor() as c:
      sql = "SELECT * from funcionario"
      c.execute(sql)
      funcioex = len(c.fetchall())
      return funcioex
      
def separar():
   print("================================")