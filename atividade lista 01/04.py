'''
4-Faça um Programa que leia lista  de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
'''

'''
ainda falta consertar
'''

c = []
n = 0
for i in range(10):
    c.append(input(f'informe o {i+1}º caracter: '))
    if c != 'a' and c!= 'e'and c!='i' and c!='o' and c!='u':
        n += 1
print(f'\nnº de consoantes lidas = {n}\n')
if n > 0:
    for i in range(10):
        if c != 'a' and c!= 'e'and c!='i' and c!='o' and c!='u':
           print(f'{i+1}º caracter: {c[i]}') 
