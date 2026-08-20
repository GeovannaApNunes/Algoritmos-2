def calc(num1,):
    if num1 > 0:
        return 'Positivo'
    elif num1 == 0:
        return 'Neutro'
    elif num1 < 0:
        return 'Negativo'

num1 = int(input("Digite um numero: "))

print(f"{calc(num1)}")
