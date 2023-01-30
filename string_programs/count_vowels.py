# a e i o u
count=0
# s="hello"
s=str(input('enter the word to check for vowels'))
v="aeiou"
for i in s:
    if i in v:
        count+=1
print(count)