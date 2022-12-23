import pymysql.cursors
connection = pymysql.connect(host='localhost', user='root', password='1234', database='prova03', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

class Funcao:
  def __init__(self, Codigo, Nome):
      self.Codigo = Codigo
      self.Nome = Nome
      self.Inserir()

  def Inserir(self):
      with connection.cursor() as c:
        sql = "INSERT INTO funcao (cod, nome) VALUES (%s, %s)"
        c.execute(sql,(self.Codigo, self.Nome))
      # connection.commit()

class Funcionario:
  def __init__(self, Nome, CPF, Funcao, Salario, Telefone):
      self.Nome = Nome
      self.CPF = CPF
      self.Funcao = Funcao
      self.Salario = Salario
      self.Telefone = Telefone
      self.InserirFuncio()

  def InserirFuncio(self):
      with connection.cursor() as c:
         sql = "INSERT INTO funcionario (cpf, nome, funcao, salario, telefone) VALUES(%s, %s, (SELECT id FROM funcao WHERE cod = %s), %s, %s)"
         c.execute(sql,(self.CPF, self.Nome, self.Funcao, self.Salario, self.Telefone))
      connection.commit()