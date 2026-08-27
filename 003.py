def maior_salario():
    nomeMaior = ""
    salarioMaior = 0.0

    for i in range(1,10):
        nome = input("Qual seu nome? ")
        salario = float(input("Qual o seu salário? "))

        if salario > salarioMaior:
            salarioMaior = salario
            nomeMaior = nome

    return nomeMaior

resultado = maior_salario()
print(f"O funcionário com maior salário é: {resultado}")
