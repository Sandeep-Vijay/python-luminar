a=open('data.txt')
l=[]
for i in a:
    data=i.rstrip('\n').split(' ')
    l.extend(data)
print(l)