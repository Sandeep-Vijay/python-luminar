# regular expression

# pattern matching

#re
import re   #inbuild method to find matches = finditer in method re-regular expression
x='[abcC]'
matcher=re.finditer(x,'abc @123ABfgh') #first string content'ab' is the content to be checked in the next string content
count=0
for i in matcher:
    count+=1
    print(i.group())
    print(i.start())
print('count',count)




