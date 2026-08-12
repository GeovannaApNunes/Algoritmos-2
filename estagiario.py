total = 0


for i in range(1,6):
    periodo = int(input('Digite o perido do estagiario: '))
    est = float(input('Digite o valor do salario do estagiario: '))
    total = est + total

print("O salario total dos estagiarios e {:.2f}".format(total))
