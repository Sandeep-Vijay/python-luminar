#simple calculator

print(' ~~~CALCULATOR~~~')

#functions for operations

def addition(num1,num2):
    return num1+num2

def subtraction(num1,num2):
    return num1-num2

def division(num1,num2):
    return num1/num2

def multiplication(num1,num2):
    return num1*num2

while True:
    choice=int(input('select operation\n1.addition\n2.subtraction\n3.division\n4.multiplication\n5.stop\nEnter your choice>>>'))
    if choice==5:
        break
    # if choice in ('1','2','3','4','5'):
    elif choice>=1 and choice<=4:
        num1 = int(input('enter the first number ='))
        num2 = int(input('enter the second number ='))
        if choice==1:
            print('> Addition <')
            print(num1,'+',num2,'=',addition(num1,num2))

        if choice ==2:
            print('> Subtraction <')
            print(num1, '-', num2, '=', subtraction(num1, num2))

        if choice ==3:
            print('> Division <')
            print(num1, '/', num2, '=', division(num1, num2))

        if choice ==4:
            print('> Multiplication <')
            print(num1, 'x', num2, '=', multiplication(num1, num2))
    else:
        print('Invalid Input')












