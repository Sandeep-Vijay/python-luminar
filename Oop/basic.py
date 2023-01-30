#oop object oriented programming

# class     -design/blueprint/structure
# object    -real-world entity
# reference -to store object
#creating class of name Person
class Person:     #class name must start with a Capital letter//class ClassName
    def walk(self):   #self is a default 'instance keyword' for method.
        print('person is walking')
    def read(self):
        print('person is reading')   #we can change self to another name


#calling the method by creating objects and stored in references
pe1=Person()   #pe1-reference #Person()-object// className()

pe1.read()      #dot is used when calling method// reference.methodName()
pe1.walk()

pe2=Person()

pe2.walk()
pe2.read()