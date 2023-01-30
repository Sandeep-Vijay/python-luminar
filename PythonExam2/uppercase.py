# -string starting and ending with a uppercase letter -except special characters  -minimum length 5  -maximum length 10
import re
x='^[A-Z][\w]{3,8}[A-Z]$'
s=input('enter the string')
matcher=re.fullmatch(x,s)
if matcher is not None:
    print('VALID')
else:
    print('INVALID')