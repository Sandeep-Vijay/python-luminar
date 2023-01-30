

# -----------------------------------------

# >>> PROTECTED MEMBER
#     The protected member is accessible from inside the class and its subclass.
#     Define a protected member by prefixing the member name with an underscore
#     Eg: _name

class Base:
    def __init__(self):
        self._a = 2

class subclass(Base):
    def __init__(self):
        Base.__init__(self)
        print(self._a)

        self._a = 3
        print(self._a)

obj1=Base()
obj2=subclass()

# -------------------------------------


