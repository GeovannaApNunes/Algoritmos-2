def mult(a,b):
    if b == 1:
        return a
    else:
        print("a", a, "b", b)
        return a + mult(a, b-1)

print(mult(3,4))