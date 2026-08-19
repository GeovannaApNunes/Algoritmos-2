def reajusteSalario(salario, setor):
    setor =setor.upper()
    if setor == 'A':
        bonus = 50
    elif setor ==  'B':
        bonus = 100
    else:
        bonus = 150

    return salario + bonus


salario = float(input("Informe o seu salario: "))
setor = input("Informe o Setor que voce trabalha: ")

r = reajusteSalario(salario, setor)
print(f"Novo Salario R$ {r}")

'''.lower() deixa as letras minusculas
   .upper() deixa as letras maiusculas
'''