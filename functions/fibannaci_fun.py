def fibanacci(limit):
    n1 = 0
    n2 = 1
    for i in range(limit):
        print(n1)
        n3 = n1 + n2
        n1 = n2
        n2 = n3

fibanacci(7)  