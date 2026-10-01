def crecente(n):
    if n == 1:
        return 1
    else:
        return f"{crecente(n - 1)} {n}"

print(crecente(4))