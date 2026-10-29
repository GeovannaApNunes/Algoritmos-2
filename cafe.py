def cafe(x, y):
    if x==y:
        return 1
    else:
        return 1 + cafe(x - y, y)

print(cafe(10, 2))