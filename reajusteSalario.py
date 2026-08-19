def reajusteSalario(salario, indice):
    aumento = salario * indice / 100
    return salario + aumento

salario = float(input("Informe o seu salario: "))
indice = float(input("Informe o indice do seu aumento: "))

r = reajusteSalario(salario, indice)

print(f"Novo Salario R$" , r)
