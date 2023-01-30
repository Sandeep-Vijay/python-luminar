# num=int(input('enter the number to check'))
# flag=0
# for i in range(2,num):
#     if i%num==0:
#         flag=1
#         break
# if flag==1:
#     print('non prime number')
# else:
#     print("prime number")


num=int(input('enter the number to check'))

for i in range(2,num):
    if num%i==0:                      ## for                        if break doesn't work else will work
                                       #     break                  if break works else will not work
                                     # else                       if we use break in a for loop we can use else
        print('non prime number')
        break
else:
    print('prime number')



