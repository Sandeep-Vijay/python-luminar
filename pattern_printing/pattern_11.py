#    *
#   * *
#  *   *
# * * * *
n=5
for i in range(5):
    for j in range(n):
        print("",end=' ')
    n=n-1
    for j in range(i):
        if(i,j)==(3,1):
            print('  ',end="")
        else:
            print('*',end=' ')
    print()
