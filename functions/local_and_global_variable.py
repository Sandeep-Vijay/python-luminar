#local and global variable

num=50

def PrintNum():
    global num,x
    x=5
    num=100
    print(num)
PrintNum()
print(num)