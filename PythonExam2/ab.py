import re
x='^a[\d]*b$'
s=input('enter the string')
matcher=re.fullmatch(x,s)
if matcher is not None:
    print('valid')
else:
    print('invalid')