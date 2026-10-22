def seq(n):
    if n == 1:
        return "1/3"
    else:
        return seq(n-1) + " + " +"1/" + str(n *4 )

print(seq(5))
