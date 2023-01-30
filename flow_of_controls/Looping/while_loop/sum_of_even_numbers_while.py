initial=int(input('enter the initial value'))
final=int(input('enter the final value'))
sum=0
while initial<=final:
    if initial%2==0:
        sum=sum+initial
    initial+=1
print(sum)

