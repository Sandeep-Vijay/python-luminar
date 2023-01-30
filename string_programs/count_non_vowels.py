v='aeiou'
s=input('enter the string')
count=0
for i in s:
    if i not in v:
        count+=1
print(count)