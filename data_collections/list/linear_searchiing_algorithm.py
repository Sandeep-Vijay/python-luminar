#linear searching algorithm
l=[1,2,3,4,5,6,8,9]

def linearsearch(e):
    count=0
    for i in l:
        count+=1
        if i==e:
            print('present')
            break

    else:
        print('not present')
    print(count)
linearsearch(8)
