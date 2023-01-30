import re
f=open('phonenumber.txt','r')
x='[+][9][1][0-9]{10}'
f1=open('valid num','w')
for i in f:
    num=i.rstrip('\n')
    match=re.fullmatch(x,num)
    if match is not None:
        f1.write(i)