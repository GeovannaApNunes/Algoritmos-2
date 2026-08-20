def calc(num1, num2, operador):
    op = operador.upper()
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        if num2 == 0:
            return "Erro: Divisão por zero"
        return num1 / num2
    else:
        return "Operador inválido"

num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))
operador = input("Digite o operador: ")

total = calc(num1, num2, operador)
print(f"Resultado: {total}")