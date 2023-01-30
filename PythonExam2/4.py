class Animal:
    def __init__(self,name,age):  #constructor
        self.name=name
        self.age=age
class Dog(Animal):
    def __init__(self,name,age):
        super().__init__(name,age)
    def printdata(self):
        print(self.name,self.age)
D=Dog('jimmy','2years')
D.printdata()