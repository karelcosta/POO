'''
3-Faça um Programa que leia 4 notas, adicione em uma lista 
e mostre as notas e a média na tela.
'''
notas = []
media = 0
for i in range(4):
    notas.append(float(input(f'informe a {i+1}ª nota: ')))
    media += notas[i]
for i in range(4):
    print(f'{i+1}ª nota: {notas[i]}')
print('media: ', media/4)