initial=int(input('enter the initial value'))
final=int(input('enter the final value'))


sum=0
for i in range(initial,final+1):
    if i%2==0:
        sum+=i
print(sum)

