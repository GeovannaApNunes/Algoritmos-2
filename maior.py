def calculamaior(a, b, c):
    if a > b and a > c:
        return a

    elif b > a and b > c:
        return b
       
    elif c > a and c > b:
        return c

a = float(input('Valor de a: '))
b = float(input('Valor de b: '))
c = float(input('Valor de c: '))

maior = calculamaior(a, b, c)

print(f'O maior numero é: {maior}')