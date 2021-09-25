class Example:
    age = 27
    name = 'Alex'
    def __init__(self, a, n):
        self.a = a
        self.n = n
    def f_2(self):
        return self.a+self.n
    def f_3(self):
        return self.a**self.n
ex = Example(4,6)
de = Example(8,9)
print(ex.f_2())
print(de.f_2())
print(ex.f_3())
print(de.f_3())