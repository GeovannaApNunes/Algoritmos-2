def div(a, b):
    if a<b:
        return 0
    else:
        print("a", a, "b", b)
        return 1 + div(a - b, b)


print(div(10, 2))
