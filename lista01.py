def seq(n):
    if n ==1:
        return "1/3"
    else:
        return seq(n-1) + "+" + str(n) + "/" + str(n+2)

print(seq(5) )