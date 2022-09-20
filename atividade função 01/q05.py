'''
5.Faça uma função que receba a altura e o raio de um cilindro circular e retorne o volume do cilindro.
'''
def calcular_vol_cilindro(al, r):
    return al * area_da_base(r)

def area_da_base(r):
    return 3.14 * (r * r)

al = float(input('informe a altura e o raio do cilindro em cm\naltura: '))
raio = float(input('raio:'))
print(f'volume do cilindro = {calcular_vol_cilindro(al, raio)}cm')