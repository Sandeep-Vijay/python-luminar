#constructor

# to initialise an object at the time of object creation

class Person:
    def __init__(self,name,age,place):  #constructor
        self.name=name
        self.age=age
        self.place=place
    def printdata(self):
        print(self.name,self.age,self.place)
pe1=Person('amal',23,'kochi')
pe1.printdata()