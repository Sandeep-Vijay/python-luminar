# 0 1 1 2 3 5 8
limit = int(input('enter the limit'))
n1 = 0
n2 = 1
for i in range(limit):
    print(n1)
    n3 = n1 + n2
    n1 = n2
    n2 = n3
