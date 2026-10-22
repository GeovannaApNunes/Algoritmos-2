def div(a, b):
    if a<b:
        return a
    else:
        print("a", a, "b", b)
        return 1 + div(a - a, b)


print(div(7, 2))