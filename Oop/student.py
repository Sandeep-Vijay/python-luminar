

class Students:
    def __init__(self,name,roll,mark):
        self.name=name
        self.rollno=roll
        self.mark=mark
    def print(self):
        print(self.name,'\n',self.rollno,'\n',self.mark,'\n')
stu=open('student.txt','r')
for i in stu:
    data=i.rstrip('\n').split(',')
    # print(data)
    name=data[0]
    roll=data[1]
    mark=data[2]
    obj=Students(name,roll,mark)
    obj.print()