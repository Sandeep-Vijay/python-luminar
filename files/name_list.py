n=open('name.txt','r')
name=[]
for i in n:
    data=i.rstrip('\n')
    if i[0]=='a':
        name.append(data)
print(name)
