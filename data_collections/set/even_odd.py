s={1,2,3,4,5,7,8,87,54,23,12}

#even
So=set()
Se=set()
for i in s:
    if i%2==0:
        Se.add(i)
    else:
        So.add(i)
print(Se,'even set')
print(So,'odd set')

# #odd
#
# So=set()
# for i in s:
#     if i%2!=0:
#         So.add(i)
# print(So,'odd set')