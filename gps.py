def calculaImposto(salario):
    g = salario * 0.27
    return g

salario = float(input("Informe o seu salario: "))

gps = calculaImposto(salario)

print(f"Imposto R$" , gps)