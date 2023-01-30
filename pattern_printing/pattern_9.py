# * * * *
#  * * *
#   * *
#    *
n=4
for i in range(5):
    for j in range(i):
        print("",end=" ")
    for j in range(n):
        print('*',end=' ')
    n=n-1
    print()