#multiple inheritance

#more than one parent

class A:
    def methodA(self):
        print('inside A class')
class B:
    def methodB(self):
        print('inside B class')
class C(A,B):
    def methodC(self):
        print('inside C class')
objC=C()
objC.methodC()
objC.methodA()
objC.methodB()