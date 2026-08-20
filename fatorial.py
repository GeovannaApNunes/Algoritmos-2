def calculaFatorial(n):
    fatorial = 1
    for i in range(1, n+1):
        fatorial *= i
    return fatorial


num = int(input("Numero do fatorial: "))
print(f"Fatorial do {num} = {calculaFatorial(num)}")