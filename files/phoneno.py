p=open('phonenumber.txt','r')
for i in p:
        data=i.rstrip('\n')

        if len(data) == 10:
            print(data)