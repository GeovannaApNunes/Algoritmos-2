'''
Calcular a area do triangulo
'''
def calculaAreaTriangulo(b,ba):
    r= b*ba
    return r 

base1 = int(input("Digite o valor da Base1: "))
base2 = int(input("Digite o valor da Base2: "))

a = calculaAreaTriangulo(base1, base2)

print("Area: " , a)