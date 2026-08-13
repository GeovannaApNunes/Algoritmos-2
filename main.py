import math

def calculamaior(cateto_a, cateto_b):
    hip = math.sqrt((cateto_a ** 2) + (cateto_b ** 2))
    return hip 

a = float(input('Valor de a: '))
b = float(input('Valor de b: '))
c = float(input('Valor de c: '))]

hipotenusa = calculamaiora(a, b, c)

print(f'O valor de hipotenusa é: {hipotenusa}')