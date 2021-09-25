class Calc:
    def __init__(self):
        self.func4()
    def func(self):
        return self.a + self.b
    def func1(self):
        return self.a - self.b
    def func2(self):
        return self.a * self.b
    def func3(self):
        if self.b == 0:
            return 'error'
        else:
            return self.a / self.b
    def func4(self):
        self.a = int(input())
        self.b = int(input())

while True:

    x = input('введите знак (+.-.*./) или если вы хотите выйти из програмы n')
    if x == 'n':
        break

    calc = Calc()
    if x == "+":
        print(calc.func())
    elif x == "-":
        print(calc.func1())
    elif x == "*":
        print(calc.func2())
    elif x == '/':
        print(calc.func3())