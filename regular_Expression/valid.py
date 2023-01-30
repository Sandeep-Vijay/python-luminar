import re
x='[0-9]{10}'
s=input('enter the string to validate')
matcher=re.fullmatch(x,s)    #fullmatch method is not iterable it is used to check matching
if matcher is not None:
    print('valid')
else:
    print('Invalid')

