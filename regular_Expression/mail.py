import re
x='\w+@gmail.com'
s=open('mail.txt','r')
for i in s:
    mail=i.rstrip('\n')
    match=re.fullmatch(x,mail)
    if match is not None:
        print(mail)
