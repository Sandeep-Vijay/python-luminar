
class Person:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def print(self):
        print(self.name,self.age,self.place)

class Student(Person):
    def __init__(self,name,age,place,roll,dep,coll):
        super().__init__(name,age,place)
        self.roll=roll
        self.dep=dep
        self.coll=coll
    def printStu(self):
        print(self.name,self.age,self.place,self.roll,self.dep,self.coll)

S1=Student('anu',23,'kochi',1,'civil','ilahia')
S1.printStu()