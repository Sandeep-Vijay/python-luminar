#5! 5*4*3*2*1


def fact(n):
    if n==1:
        return n
    else:
        return n*fact(n-1)
print(fact(5))