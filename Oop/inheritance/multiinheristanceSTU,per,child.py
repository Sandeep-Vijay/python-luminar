class Person:
    def __init__(self,name,age,place):
        self.name=('name',name)
        self.age=('age',age)
        self.place=('place',place)
class Child:
    def __init__(self,school,phn):
        self.school=('school',school)
        self.phn=('phone No',phn)
class Student(Person,Child):
    def __init__(self,name,age,place,school,phn,roll,dep):
        Person.__init__(self,name,age,place)
        Child.__init__(self,school,phn)
        self.roll=('roll No',roll)
        self.dep=('department',dep)
    def print(self):
        print(self.name,self.age,self.place,self.school,self.phn,self.roll,self.dep)
objStu=Student('anu',21,'kochi','Luminar',9605986743,2,'civil')
objStu.print()