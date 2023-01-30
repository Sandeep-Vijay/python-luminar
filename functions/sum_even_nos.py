def sumeven(initial,final):
    sum=0
    for i in range(initial,final+1):
        if i%2==0:
            sum+=i
    return sum


print(sumeven(5,10))