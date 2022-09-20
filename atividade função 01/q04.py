'''
4.Faça uma função que receba dois números e retorne qual deles é o maior.
'''
def verificar_maior(n1, n2):
    if n1 > n2:
        return n1
    elif n2 > n1:
        return n2
    else:
        return 'ambos os numeros são do mesmo tamanho'
n1 = float(input('informe o primeiro numero: '))
n2 = float(input('informe o segundo numero: '))
print(f"\nmaior numero:\n{verificar_maior(n1, n2)}")