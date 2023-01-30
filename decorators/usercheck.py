
def checkname(func):
    def wrapper(a,b):
        if a!='admin':
            raise Exception('cannot change pin')
        else:
            return func(a,b)
    return wrapper

@checkname
def change_pin(username,pin):
    current_pin=pin
    return current_pin


print(change_pin('sanu',12344))