# map
# filter

#collection
# l=[1,2,3,4,5,6]
# output map
#


# map(funtion,iterable data)
# filter(funtion,iterable data)   #same arguments for filter and map

l=[1,2,3,4,5,6]

# create a square list from l
# map      #function must be with argument and return type
#same number of elements we need then use map



# def square(n):
#     return n**2
# new=list(map(square,l))
# new1=set(map(square,l))
# print(new)
# print(new1)


# def cube(n):
#     return n**3
# cube=list(map(cube,l))
# print(cube)


# even numbers

def even(n):
    return n%2==0
print(list(filter(even,l)))