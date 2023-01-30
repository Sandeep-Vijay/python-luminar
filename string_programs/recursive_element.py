s='hello'  #l   recursive element is the repeated element

#malayalam  aalam

# r=input('enter the word to find recursive element')
# data=''
# for i in r:
#     if i not in data:
#         data=data+i
#     else:
#         print(i)
#         break


# d=input('enter the word to find last recursive element')
# dup=''
# data=''
# for i in d:
#     if i not in data:
#         data=data+i
#     else:
#         dup=dup+i
# print(dup[-1])


d=input('enter the word to find last recursive element')
dup=''
data=''

for i in d:
    if i not in data:
        data=data+i
    else:
        if i not in dup:
            dup=dup+i
print('second recursive',dup[1])
print('first recursive',dup[0])
print('last recursive',dup[-1])
