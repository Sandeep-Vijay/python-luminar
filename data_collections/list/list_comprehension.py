#list comprehension

# l=[5,6,7,8]
# square=[]
# for i in l:
#     square.append(i**2)
# print(square)

#using list comprehension

# l=[5,6,7,9]
# square=[i**2 for i in l]
# print(square)

#even odd LC
# l=[1,2,3,4,5,6,7,8,9]
# l2=[i for i in l if i%2==0]
# print(l2,'even')
# l3=[i for i in l if i%2!=0]
# print(l3,'odd')

#1 to 50 divisible by 10 and even

num=[i for i in range(1,51) if i%2==0 and i%10==0]
print(num)