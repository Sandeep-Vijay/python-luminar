# ------------------

#>>> Public Member
#    The public member is accessible from inside or outside the class.

class Base:
    def __init__(self):
        self.a='python'
class Public:
    def __init__(self):
        Base.__init__(self)
        print(self.a)

obj=Public()

# -----------------