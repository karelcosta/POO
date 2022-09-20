'''
3.Faça uma função e um programa de teste para o cálculo do volume de uma esfera. Sendo que o raio é passado por parâmetro.
'''
def calculo_do_volume(r):
    return (4 * 3.14 * r)/3
raio = float(input('informe o raio da esfera em cm: '))
print(f"volume da esfera = {calculo_do_volume(raio)}cm")