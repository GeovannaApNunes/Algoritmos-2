def soma(a,b):
    if a == 0:
        return b
    else:
        print("a", a, "b", b)
        return soma(a-1, b+1)

print(soma(3,4))