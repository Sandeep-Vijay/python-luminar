#program to find 5 divisible numbers between the user inputed values

initial_value=int(input('enter the initial value'))
final_value=int(input('enter the final value'))

for i in range(initial_value,final_value+1):
    if i%5==0:
        print(i)