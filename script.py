def leitura():
    heroi = open('herois.txt', 'a')
    nome = input('Digite o nome do heroi: ')

    heroi.write(nome + '\n')
    heroi.close()

def formatar():
    heroi = open('herois.txt', 'r')
    report = open('report.txt', 'w')
    for h in heroi:
        report.write(h.rstrip() + 'esta presente no filme. \n')
    heroi.close()
    report.close()

leitura()
formatar()