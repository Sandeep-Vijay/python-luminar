#student name roll dep coll

#two types of variables in Oop
# 1.Instance variables -related to methods//using within methods -self
# 2.Static variables -related to class//using in class -calling using Classname

class Student:
    college='ilahia'  #it is a static variable-
    def Details(self,name,rollno,dep):
        self.name=name
        self.rollno=rollno
        self.dep=dep

    def PrintDetails(self):
        print(self.name,self.rollno,self.dep,Student.college)


de1=Student()
de1.Details('amal',1,'mech')
de1.PrintDetails()

de2=Student()
de2.Details('anu',2,'civil')
de2.PrintDetails()

