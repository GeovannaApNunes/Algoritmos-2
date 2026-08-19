def reajusteSalario(salario, setor):
    if setor == 1:
        bonus = 50
    elif setor == 2:
        bonus = 100
    elif setor == 3:
        bonus = 150
    else:
        bonus = 0

    return salario + bonus

salario = float(input("Informe o seu salario: "))
setor = int(input("Informe o Setor que voce trabalha: 1-A 2-B 3-Outros: "))

r = reajusteSalario(salario, setor)
print(f"Novo Salario R$ {r}")

'''.lower() deixa as letras minusculas
   .upper() deixa as letras maiusculas
'''