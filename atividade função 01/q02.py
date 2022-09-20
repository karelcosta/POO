'''
2.Faça uma função para verificar se um número é positivo ou negativo. Sendo que o valor de retorno será 1 se 
positivo, -1 se negativo e O se for igual a 0.
'''
def verificar_numero(n):
    if n > 0:
        return 1
    elif n < 0:
        return -1
    else:
        return 0
        
numero = float(input('informe o numero: '))
print(verificar_numero(numero))