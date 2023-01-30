#multilevel inheritance
#
class A:
    def methoda(self):
        print('inside A')
class B(A):
    def methodb(self):
        print('inside B')
class C(B):
    def methodc(self):
        print('inside c')

objC=C()
objC.methoda()
objC.methodb()
objC.methodc()

#person
#parent
#employee

class Person:
    def __init__(self,name,age,place):
        self.name=('name:',name)
        self.age=('age:',age)
        self.place=('place:',place)
class Parent(Person):
    def __init__(self,name,age,place,school,roll):
        super().__init__(name,age,place)
        self.school=('school:',school)
        self.roll=('roll No:',roll)
class Employee(Parent):
    def __init__(self,name,age,place,id,des,school,roll):
        super().__init__(school,roll,name,age,place)
        self.id=('ID:',id)
        self.des=('designaion:',des)
    def print(self):
        print(self.name,self.age,self.place,self.school,self.roll,self.id,self.des)

objE=Employee('anu',21,'kochi',1234,'developer','luminar',12)
objE.print()