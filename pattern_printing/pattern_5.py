# 1
# 2 3
# 4 5 6
# 7 8 9 10
num=0
for row in range(1,5):
    for col in range(row):
        num=num+1
        print(num,end=" ")
    print()