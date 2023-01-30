num1=float(input("Enter the first number"))
num2=float(input('Enter the second number'))

if num1<num2:
    print(num1,"is the smallest number and",num2,"is the greatest number")
elif num1==num2:
    print('both numbers are equal')
else:
    print(num2,'is the smallest number and',num1,'is the greatest number')