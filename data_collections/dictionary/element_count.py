l=[10,20,30,10,10,20,30,40,50,40,70]
c={}
for i in l:
    if i not in c:
        c[i]=1
    else:
        val=c[i]
        val+=1
        c[i]=val
print(c)