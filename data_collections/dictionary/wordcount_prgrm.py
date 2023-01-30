s='hello hi hello hi hi luminar'
# data=s.split(' ')
# print(data)
for i in s:
    data=s.split(' ')
d={}
for i in data:

    d[i]=s.count(i)
print(d)

#method 2
# data=s.split(' ')
# print(data)
# count={}
# for i in data:
#     if i not in count:
#         count[i]=1
#     else:
#         val=count[i]
#         val+=1
#         count[i]=val
# print(count)

