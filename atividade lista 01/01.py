'''
1-Faça um Programa que receba uma lista de 5 números inteiros e mostre-os.
'''
lista=[]
for i in range(5):
    lista.append(int(input(f'informe o {i+1}º valor: ')))
print(lista)