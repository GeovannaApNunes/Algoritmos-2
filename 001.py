'''Implementar uma função que retorna o nome por extenso de um mês.'''
def meses(mes):
        if mes == 1:
            return 'JANEIRO'
        elif  mes == 2:
            return 'FEVEREIRO'
        elif  mes == 3:
            return 'MARCO'
        elif  mes == 4:
            return 'ABRIL'
        elif  mes == 5:
            return 'MAIO'
        elif  mes == 6:
            return 'JUNHO'
        elif  mes == 7:
            return 'JULHO'
        elif  mes == 8:
            return 'AGOSTO'
        elif  mes == 9:
            return 'SETEMBRO'
        elif  mes == 10:
            return 'OUTUBRO'
        elif  mes == 11:
            return 'NOVEMBRO'
        elif  mes == 12:
            return 'DEZEMBRO'
        else:
            return 'MES INVALIDO'

mes = int(input('Qual mes voce deseja? (Digite de 1 a 12): '))
meses = meses(mes)

print(f"O mes desejado e: {meses}")