#functions
#identifier variables data
#           function_name


#1.function without argument
# def  add():                                    #function is defined by def keyword
#     num1=int(input('enter the num1'))
#     num2 = int(input('enter the num2'))
#     print('sum',num1+num2)
# add()
#


#2. funtion with argument
#
# def add(num1,num2):
#     print('sum',num1+num2)
# no1=int(input('enter no1'))
# no2=int(input('enter no2'))
#
# add(no1,no2)
# add(1,2)


#3. function with argument and return type
# def add(num1,num2):
#     return num1+num2    #when return-then the working of that function will stop then no remaining code will be executed
# print(add(2,4))         #we can use only one return for each block
# sum=add(2,5)            #when returns a value use only one value,no two values are accepted
# print(sum)



def printi(n):
    for i in range(n):
        return i
                              #programs that need iteration cannot be done by return type function
print(printi(5))



