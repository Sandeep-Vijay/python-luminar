# decorators-change the working of functions without changing the actual function

def swapvalue(func):
    def wrapper(a,b):
        if a<b:
            a,b=b,a
            return func(a,b)
        else:
            return func(a,b)
    return wrapper
@swapvalue
def substract(n1,n2):

        print(n1-n2)
substract(3,5)
substract(20,10)
substract(30,300)

@swapvalue
def division(n1,n2):
    print(n1/n2)
division(2,10)