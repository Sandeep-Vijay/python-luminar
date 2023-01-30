# string_programming

s="luminar technolab"
print(s)
print('count of letter a')
count=0
for i in s:
    # print(i)   #for loop can be also used to iterate each elements in a string
    if i == "a":
        count+=1
print(count,'numbers')