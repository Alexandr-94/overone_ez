class Db:
    def __init__(self, one=None , two=None, three=None):
        self.one = one
        self.two = two
        self.three = three
    def g(self,a,b,c):
        self.one = a
        self.two = b
        self.three = c
        print(self.one, self.two, self.three)

db=Db()
db.g(1,None,None)
db.g(1,2,None)
db.g(None,None,3)


