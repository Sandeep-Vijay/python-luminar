

from abc import ABC,abstractmethod

class Car(ABC):               # ABSTRACT CLASS
    @abstractmethod
    def mileage(self):        # ABSTRACT METHOD
        pass


class Tesla(Car):
    def mileage(self):
        print("Tesla's mileage is 30kmph")

class Suzuki(Car):
    def mileage(self):
        print("Suzuki's mileage is 25kmph ")

class Ford(Car):
    def mileage(self):
        print("Ford's mileage is 24kmph ")

class Renault(Car):
    def mileage(self):
        print("Renault's mileage is 27kmph ")

t = Tesla()
t.mileage()

r = Renault()
r.mileage()

s = Suzuki()
s.mileage()

F = Ford()
F.mileage()

# -------------------
