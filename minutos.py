def calculaMin(horas):
    min =  horas * 60
    return min
def calculaSegundos(horas):
    segundos = horas * 3600
    return segundos

horas = float(input("Informe o total de horas: "))

minutos = calculaMin(horas)
segundos = calculaSegundos(horas)

print(f"Minutos: " , minutos)
print(f"Segundos: " , segundos)