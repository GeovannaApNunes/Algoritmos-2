def seq(n):
    if n == 1:
        return "1/1"
    else:
        return seq(n-1) + " + " + str(n) +"/" + str(n*n)

print(seq(5))
