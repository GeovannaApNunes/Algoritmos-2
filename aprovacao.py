def calc(nota,):
    if nota >= 60:
        return 'Aprovado'
    elif nota >= 40 and nota < 60:
        return 'Exame especial'
    elif nota < 40:
        return 'Reprovado'

nota = int(input("Digite sua nota: "))

print(f"{calc(nota)}")
