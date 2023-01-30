v=open('name.txt','r')
v1=open('newname.txt','w')
vowels='aeiou'
for i in v:
    if i[0] not in 'aeiou':
        v1.write(i)

