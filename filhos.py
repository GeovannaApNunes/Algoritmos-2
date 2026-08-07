'''print("Digite a quantidade de filhos do Miguel: ")
miguel = int(input())

print("Digite a quantidade de filhos do Abel: ")
abel = int(input())

netos = abel + miguel

print('A quantidade de filhos de Miguel é' ,miguel, 'A quantidade de filhos de Abel é ' ,abel)
print('A quantidade de netos do Arnaldo é ',netos)

# Útil para templates ou versões antigas do Python
texto = "O {0} custa {1} reais.".format("livro", 45)
print(texto)
'''

# Expressões matemáticas e variáveis direto nas chaves
preco = 49.9
print(f"O valor com desconto é R$ {preco * 0.9:.2f}")


print("Digite o valor da aposentadoria recebida: ")
apos = float(input())

print("Digite o valor do aluguel recebido: ")
alu = float(input())

total = alu + apos

print(f'O total recebido é de R${total:.2f}')

