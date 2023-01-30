

#>>> PRIVATE MEMBER
#    private member is accessible only inside class.
#    Define a private member by prefixing the member name with two underscores
#    Eg: __name

class Base:
    def __init__(self):
        self.a = "Luminar"
        self.__c = "Python"
    def print(self):
        print(self.__c)
class Subclass(Base):
    def printsubclass(self):
        Base.__init__(self)
        print(self.a)
        print(self.__c)
obj1=Base()
obj1.print()

obj2=Subclass()
obj2.printsubclass()