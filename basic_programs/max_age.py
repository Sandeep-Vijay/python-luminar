person=[('anu',23),('amal',21),('arun',26),('vineeth',22)]
n=[]
for i in person:
        n.append(i[1])
maxage=max(n)
for i in person:
    if i[1]==maxage:
        print(i[0])