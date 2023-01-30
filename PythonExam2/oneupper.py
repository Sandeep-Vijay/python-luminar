import re
x='[A-Z]+[a-z]+$'
s=input('enter the string')
matcher=re.fullmatch(x,s)
if matcher is not None:
    print('VALID')
else:
    print('INVALID')