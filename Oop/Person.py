class Person:
    def setvalue(self,name,age,place):    #creating arguments
        self.name1 = name
        self.age=age
        self.place=place

    def printvalue(self):
        print(self.name1)
        print(self.age)
        print(self.place)

pe1=Person()
pe1.setvalue('sugu',22,'kochi')
pe1.printvalue()

pe2=Person()
pe2.setvalue('amal',23,'kakkanad')
pe2.printvalue()