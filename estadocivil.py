estado = input('Digite seu estado civil (C , S , D, V): ')

if estado == 'C' or estado == 'c':
    print('Você é casado(a) - Valido')

elif estado == 'S' or estado == 's':
    print('Você é solteiro(a) - Valido')

elif estado == 'D' or estado == 'd':
    print('Você é divorciado(a) - Valido')

elif estado == 'V' or estado == 'v':
    print('Você é viuvo(a) - Valido')
    
else:
    print('INVALIDO')
