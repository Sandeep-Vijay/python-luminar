#polymorphism

# poly means many
# morphism means forms

# methods

#1.overloading
#methods name are same and different number of arguments

# class A:
#     def method(self,n):
#         self.n=n
#         print('inside A')
# class B(A):
#     def method(self):
#         print('inside B')
# objB=B()
# objB.method(12) #method in A will work
# objB.method()   #method in B will work

#the number of arguments determines which method is going to work

#recently python will not accept overloading concept but need to study the concept

#2.over-riding
#same method name and same number of arguments

class Parent:
    def buyphone(self):
        print('buy nokia')
class Child(Parent):
    def buyphone(self):
        print('buy iphone')
class Child2(Child):
    def buyphone(self):
        print('buy oneplus')
objChild=Child2()
objChild.buyphone()   #child class method will work