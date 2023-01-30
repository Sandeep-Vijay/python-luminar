

def agecheck(function):
    def wrapper(a,b):
        if b<18:
            raise Exception(a,'is not eligible')

        else:
            return function(a, b)
    return wrapper

@agecheck
def vaccination(name,age):
    print('vaccinated successfully')
@agecheck
def drivinglicense(name,age):
    print('you can take test')

vaccination('anu',18)
drivinglicense('amal',20)