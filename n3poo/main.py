from Funcoes import *
while True:
   menuIni()
   op = None
   try:
      op = int(input("Escolha uma opção: "))
      if op == 1:
         menufunc()
      elif(op == 2):
         menufuncionario()
      elif(op == 0):
         print("Saindo")
         break
      else:
         print('opção invalida')
   except:
      print('opição invalida')

   
   