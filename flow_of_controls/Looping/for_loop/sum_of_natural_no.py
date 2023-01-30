initial_value=int(input('enter the initial value'))
final_value=int(input('enter the final value'))

sum=0  #initialising sum
for i in range(initial_value,final_value+1):
    sum=sum+i  #if we already use one variable to change the same variable need to initialise
 #sum+=1
print(sum)