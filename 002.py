'''Implementar uma função que recebe os números romanos e retorna por extenso de 1 a 10.'''
def troca(rom):
    rom = rom.lower()
    if rom == 'i':
        return '1'
    elif rom == 'ii':
        return '2'
    elif rom == 'iii':
        return '3'
    elif rom == 'iv':
        return '4'
    elif rom == 'v':
        return '5'
    elif rom == 'vi':
        return '6'
    elif rom == 'vii':
        return '7'
    elif rom == 'viii':
        return '8'
    elif rom == 'ix':
        return '9'
    elif rom == 'x':
        return '10'
    else:
        return 'NUMERO INVALIDO'


rom = input('Qual numero voce deseja converter: ')
num = troca(rom)

print(f"O numero e: {troca(rom)}")