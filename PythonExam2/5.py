# over-riding
#same method name and same number of arguments
class Book:
    def buyBook(self):
        print('buy Bk1')
class Note(Book):
    def buyBook(self):
        print('buy Bk2')
class Paper(Note):
    def buyBook(self):
        print('buy Bk3')
obj=Paper()
obj.buyBook()
#child class method will work