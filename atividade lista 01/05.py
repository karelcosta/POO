'''
5-Faça um Programa que leia 20 números inteiros e armazene-os uma lista. Armazene os números pares na lista PAR
e os números IMPARES na lista impar. Imprima as três listas.
'''
lista = []
par = []
impar = []
np = 0
ni = 0
print('informe 20 numeros inteiros:')
for i in range(20):
    lista.append(int(input(f'informe o {i+1}º numero: ')))
    if lista[i]%2 == 0:
        par.append(lista[i])
        np += 1
    else: 
        impar.append(lista[i])
        ni += 1
print('\ntodos os numeros:\n')
for i in range(20):
    print(f'{i+1}º: {lista[i]}')
print('\nnumeros pares:\n')
for i in range(np):
    print(f'{i+1}º: {par[i]}')
print("\nnumeros impares:\n ")
for i in range(ni):
    print(f'{i+1}º: {impar[i]}')