s={4,5,6,7,8,9,10,15,16,20,30}
s1=set()
for i in s:
    if i%2==0 and i%5==0:
        s1.add(i)
print(s1)