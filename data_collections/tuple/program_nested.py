employee=(('anu','dev',50000),('amal','dev',57000),('anil','tester',34000))
for i in employee:
    if i[-1]>55000:
        print(i,'salary above 55000')
print('developers are:')
for i in employee:
    if i[1]=='dev':
        print(i[0])

print('least salary employee')
s=[]
for i in employee:
    s.append(i[-1])
print(s)
min=min(s)
for i in employee:
    if min==i[-1]:
        print(i[0],'has the lowest salary of',i[-1])
