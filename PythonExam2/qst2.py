class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Student(Person):
    pass
class Child(Student):
    pass
class Final(Child,Person):
    def __init__(self, name, age, coll):
        super().__init__(name, age)
        self.coll = coll
    def printStu(self):
        print(self.name, self.age, self.coll)

obj=Final('sandeep',22,"Luminar")
obj.printStu()