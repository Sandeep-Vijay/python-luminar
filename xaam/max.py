students=[('anu',67),('amal',69),('arun',65)]
n=[]
for i in students:
        n.append(i[1])
maxmark=max(n)
for i in students:
    if i[1]==maxmark:
        print(i[0])