#pair sum

sum=int(input('enter the sum'))

for i in range(6):
    for j in range(6):
        if i+j==sum:
           print(i,j)

