#swap

num1=float(input('enter num1'))
num2=float(input('enter num2'))
print('before swapping num1 is',num1)
print('before swapping num2 is',num2)

# #method 1
# temp=num1
# num1=num2
# num2=temp

#method 2
#tuple unpacking    #best option to use in python
num1,num2=num2,num1

print('after swapping num1 is',num1)
print('after swapping num2 is',num2)

#method 3  num1=5  num2=10
num1=num1+num2    #num1=15
num2=num1-num2    #num2=5
num1=num1-num2    #num1=10

