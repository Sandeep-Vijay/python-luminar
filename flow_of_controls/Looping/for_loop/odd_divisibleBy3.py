initial_value=int(input('enter the initial value'))
final_value=int(input('enter the final value'))

for i in range(initial_value,final_value+1):
    if i%2!=0:     #also can be done by using 'and' operation
        if i%3==0:
            print(i)
