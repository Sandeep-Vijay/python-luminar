d={'name':'anu','age':23,'place':'kochi'}
print(d)
print(type(d))
# print(d[0])  indexing not supported
print(d['name'],d['age']) #can call value

for i in d:
    print(i,d[i])

print(d.keys())
print(d.values())
#empty set
d2={}
d1=dict()
print(d2)
print(type(d1))

#methods to add or remove elements from dictionary

# method 1 to add

d2.update({'name':'sugu','age':32})
print(d2)

#method 2 to add

d2['place']='kochi'
print(d2)

d2['phn']=9605985701
print(d2)
d2['phn']=9447821728
print(d2)

# methods to remove element from dictonary

#single element

del d2['age']
print(d2)
#total element delete

d2.clear()
print(d2)


#delete dictionary
# del d2
# print(d2)
