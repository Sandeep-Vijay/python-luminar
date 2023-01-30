words=open('WordCount.txt')

for i in words:
    data=i.split(' ')
d={}
for i in data:
    d[i]=data.count(i)
print(d)