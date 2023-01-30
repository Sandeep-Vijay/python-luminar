
#sorting in ascending order

l1=[5,1,2,7,9,2,7,3]
# l2=[]
# while l1:     #while function remains true until the data collection becomes empty.if the data collection is empty while function becomes false and loop will not work
#     min=l1[0]
#     for j in l1:
#         if j<min:
#             min=j
#     l2.append(min)
#     l1.remove(min)
# print(l2)

l1.sort()
print(l1)


#descending order
# l2=[]
# while l1:
#     max=l1[0]
#     for j in l1:
#         if j>max:
#             max=j
#     l2.append(max)
#     l1.remove(max)
# print(l2)
#


print(l1[::-1])

