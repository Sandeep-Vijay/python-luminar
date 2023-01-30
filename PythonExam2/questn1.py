class Vehicle:
    def __init__(self, name, mileage):
        self.name=name
        self.mileage=mileage
class Bus(Vehicle):
    def __init__(self,name,mileage,speed):
        super().__init__(name,mileage)
        self.speed=speed
    def printdetails(self):
        print(self.name,self.mileage,self.speed)
objBus=Bus('Bus','20km','40kmph')
objBus.printdetails()