que=[]
size=int(input ('enter size of que>>>'))
top=0
def enqueue():
    global top
    if top>=size:
        print("que is full")
    else:
        e=int (input ("enter element to add>>>"))
        que.append (e)
        top+=1
        print(que)
def dequeue():
    global top
    if top==0:
        print('que is empty')
    else:
        que.remove(que[0])
        top-=1
        print(que)

while True:
    opt=int(input('select operation\n1.enqueue\n2.dequeue'))
    if opt==1:
        enqueue()
    else:
        dequeue()