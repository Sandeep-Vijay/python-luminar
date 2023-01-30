class Productsdetails:
    def __init__(self,num,name,price):
        self.name=name
        self.price=price
        self.num=num
    def print(self):
            print(self.num,self.name,self.price)
details=open('products.txt','r')
Max=0
for i in details:
    data=i.rstrip('\n').split(',')
    num=data[0]
    name=data[1]
    price=int(data[2])
    obj=Productsdetails(num,name,price)
    if price>Max:
        Max=price
print(Max)
