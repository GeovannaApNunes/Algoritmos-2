def calculaI(valor):
    g = valor * 0.18
    return g

valor = float(input("Informe o valor do produto: "))

icms = calculaI(valor)

print(f"ICMS R$" , icms)