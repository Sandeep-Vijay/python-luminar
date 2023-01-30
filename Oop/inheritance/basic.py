#inheritance

#inheriting(to use the properties) the properties of one class to another class
#properties are obj and variables in it
#single inheritance /one child has only one parent class
class Vehicle:  #parent class/super class/base class
    def drive(self):
        print('Engine is working')
class Bus(Vehicle):    #B inherits the properties of A class  #child class/sub class/derived class
    def moving(self):
        print('bus is moving')

objB=B()
objB.methodA(100)
objB.methodB()