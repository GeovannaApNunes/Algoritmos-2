pergunta = 'S'
while pergunta == 'S':
    nome = input('Digite o nome do Funcionario: ')
    func.write(nome + '\n')
    pergunta = input('Deseja continuar digitando? [S/N] : ')
func.close()

func = open('nomes.txt', 'r')

if re.search('Caixeta', nome, re.IGNORECASE):
    print("A string tem Caixeta")
else:
    print("A string não tem Caixeta")



func.close()