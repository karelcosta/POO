'''
2-Faça um Programa que receba uma lista de 10 números reais 
e mostre-os na ordem inversa.
'''
lista = []
for i in range(10):
    lista.append(float(input(f'informe o {i+1}º número da lista: ')))
lista.reverse()
print(lista)