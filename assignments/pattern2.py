
n=5
for i in range(1,7):
    for j in range(n):
        print(' ',end='')
    n-=1
    for j in range(i):
        print('*',end=' ')
    print()
n=5
for i in range(0,6):
    for j in range(i+1):
        print('',end=' ')
    for j in range(n):
        print('*',end=' ')
    n-=1
    print()