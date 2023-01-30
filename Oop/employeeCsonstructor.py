class Employee:
    def __init__(self,name,id,designation):
        self.name=name
        self.id=id
        self.desig=designation
    def print(self):
        print('name:',self.name,'\n','ID:',self.id,'\n','Role:',self.desig,'\n')
E1=Employee('farhan',9574,'developer')
E1.print()