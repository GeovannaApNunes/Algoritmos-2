def lerDados():
    nome = open('clientes.txt', 'a')
    endereco = open('endereco.txt', 'a')
    titulo = open('duplicata.txt', 'a')

    for i in range(3):
        n = input('Digite o nome do cliente: ')
        e = input('Digite o endereco do cliente: ')
        t = input('Digite o valor do titulo a receber do cliente: ')
        nome.write(n + '\n')
        endereco.write(e + '\n')
        titulo.write(t + '\n')

    nome.close()
    endereco.close()
    titulo.close()

def gerarCarta():
    nome = open('clientes.txt', 'r')
    endereco = open('endereco.txt', 'r')
    titulo = open('duplicata.txt', 'r')

    carta = open('carta.txt', 'w')
    for n in  nome:
        carta.write( n.upper() + '' + endereco.readline().upper() +
                 '\n\n' + "Prezado client. \n"+
                     "Consta um titulo em aberto no valor de R$"+ titulo.readline() + '\n'
                     + 'Solicitamos a sua visita a nossa loja, a fim de negociarmos sua divida \n'+
                     'Evite seu registro no SPC\n Atenciosamente, Depto cobranca\n\n\n'
                     )

##lerDados()
gerarCarta()