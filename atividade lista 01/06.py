'''
6-Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene em uma lista a média de cada aluno,
imprima o número de alunos com média maior ou igual a 7.0.
'''
notas = []
n = 0
print('informe as notas dos alunos\n')
for i in range(10):
    print(f"{i+1}º aluno: ")
    for f in range(4):
        notas.append(float(input(f'{f+1}ª nota:  ')))
print('\nmedia dos alunos\n')
for  i in range(0, 40, 4):
    media = (notas[i] + notas[i+1] + notas[i+2] + notas[i+3]) / 4          
    print(f'media do {i+1}º aluno = {media}')
    if media >= 7:
        n += 1
print('alunos com media >= 7 = ', n)

