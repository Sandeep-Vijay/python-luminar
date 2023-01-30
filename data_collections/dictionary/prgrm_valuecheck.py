d={1:100,2:200,3:300,4:400,5:500}
v=int(input('enter the value to search'))
if v in d.values():
        print('present')
else:
    print('not present')