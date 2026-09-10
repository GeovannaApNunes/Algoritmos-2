'''
aluno = open('nomes.txt' , 'a')

aluno.write('Aparecida' + '\n')
print('Nome Gravado com sucesso!')
aluno.close()
'''

pergunta = input('Deseja recriar o arquivo: ')
if pergunta.upper() == 'S':
    aluno = open('nomes.txt' , 'w')
    endereco = open('endereco.txt' , 'w')
else:
    aluno = open('nomes.txt' , 'a')
    endereco = open('endereco.txt' , 'a')
pergunta  = 'S'
while pergunta == 'S':
    nome = input('Digite o nome do aluno: ')
    aluno.write(nome + '\n')
    endereconome = input('Digite o endereco do aluno: ')
    endereco.write(endereconome + '\n')
    pergunta = input('Deseja continuar? [S/N] : ')
aluno.close()

aluno = open('nomes.txt' , 'r')
endereco= open('endereco.txt' , 'r')

maluno = aluno.readlines()
mendereco = endereco.readlines()

i=0

for i in maluno:
    print( i + 'reside' + mendereco[i])
    i=i+1


print(aluno.read() + endereco.read())
aluno.close()
endereco.close()
