# # *args
#
# def add(*args):
#     return sum(args)    #we get tuple as output
#
# print(add(20,30,30,20,10,20,30))


# **args

def printdata(**args):  #output as dictionary  #keyword arguments
    print(args)
printdata(name='anu',age=21,place='kochi',phone='96058759493')