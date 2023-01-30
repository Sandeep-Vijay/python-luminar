e=str(input('enter the element to search'))

s="luminar technolab"
# flag=0
# for i in s:
#     if i==e:
#         # break
#         flag=1
# if flag==1:
#     print('present')
# else:
#     print('not present')

if e in s:                 #in  #not in  ##the element 'e' must be a single element while using this method
    print('present')
else:
    print('not present')
