class Employee:
    company='wipro'
    #           E1    amal 9857   manager
    def Details(self,name,id,designation):
        self.name=name
        self.id=id
        self.desig=designation

    def Print(self):                         #wipro
        print(self.name,self.id,self.desig,Employee.company)
E1=Employee()
E1.Details('amal',9857,'manager')
E1.Print()

E2=Employee()
E2.Details('anu',2345,'developer')
E2.Print()

