f=open('copydata.txt','r')
w=open('data.txt','w') #if we use a new file name instead of 'data.txt'-a new file will be created with the data
for i in f:
    w.write(i)
