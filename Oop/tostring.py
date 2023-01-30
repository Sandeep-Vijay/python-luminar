
#Tostring method is used to convert the object to string ie the reference value is changed to a string value


class Student:
    college='ilahia'  #it is a static variable-
    def Details(self,name,rollno,dep):
        self.name=name
        self.rollno=rollno
        self.dep=dep

    def PrintDetails(self):
        print(self.name,self.rollno,self.dep,Student.college)
    def __str__(self):    #it is the method used to convert the reference to string
        return self.name+str(self.rollno)
de1=Student()
de1.Details('amal',1,'mech')
de1.PrintDetails()
print(de1.rollno)
print(de1.name)

de2=Student()
de2.Details('anu',2,'civil')
de2.PrintDetails()
print(de2)
