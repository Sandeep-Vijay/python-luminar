

def binarysearch(e,l):
    count=0
    flag=0
    l.sort()
    low=0
    upper=len(l)-1
    while low<=upper:
        count+=1
        midindex=(low+upper)//2
        if e==l[midindex]:
            flag=1
            break
        elif e>l[midindex]:
            low=midindex+1
        elif e<l[midindex]:
            upper=midindex-1
    if flag==1:
        print('present')
    else:
        print('not present')
    print(count)


binarysearch(8,[1,2,3,4,5,6,7,8,9])