#text files

#operations

#1.read     'r'
#2.write    'w'
#3.append   'a'

# 1.read

# f=open('data.txt','r')     #open()  used to open a txt file   'r' to which mode are using
# # print(f)
# for i in f:
#     data=i.rstrip('\n')  #used to remove any content from txt file
#     print(data)
#2.write

# f=open('data.txt','w')
# f.write('hellooo\n')
# f.write('hiiii')

#3.append
f=open('data.txt','a')
f.write('\nheeyyy')