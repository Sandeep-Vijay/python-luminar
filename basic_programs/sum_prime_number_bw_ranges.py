initial=int(input('enter the initial range'))
final=int(input('enter the final range'))
sum=0
for i in range (initial,final+1):
    if i>1:
       for j in range(2,i):
           if i%j!=0:
               sum=sum+i
               break
print(sum)
               #break
#        else:
#             sum=sum+i
# print(sum)





