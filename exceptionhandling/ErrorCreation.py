num1=int(input('enter num1'))
num2=int(input('enter num2'))
if num1<num2:
    raise Exception('negative value error')
else:
    print(num1-num2)