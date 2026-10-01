def crecente(n):
    if n == 1:
        return 1
    else:
        return f"{crecente(n - 1)} {n}"

print(crecente(4))

def decrescente(n):
    if n == 1:
        return 1
    else:
        return f"{n} {decrescente(n - 1)}"

print(decrescente(4))
