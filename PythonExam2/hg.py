import re
def decor(func):
    def wrapper(a):
        x = '[+][9][1][0-9]{10}'
        for i in x:
            num = i.rstrip('\n')
            match = re.fullmatch(x, num)
            if match is not None:
                    print('valid Number')
                    return func(a)
            else:
                raise Exception('Not valid')
                return func(a)
    return wrapper
@decor
def change_number(phn_number):
    new_number=phn_number
    return new_number
print(change_number('+911294567890'))