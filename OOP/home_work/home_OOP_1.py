class Example():
    def __init__(self):
        self.h = 0  # здесь все счетчики пишем
        self.t = 0
        self.gl = 'aieouy'
        self.ch = 0
        self.nch = 0

    def func(self, a):
        if type(a) is str:
            for i in a:
                if i in self.gl:
                    self.h += 1
                else:
                    self.t += 1
            proiz = ex.h * ex.t
            if proiz <= ex.func_1(c):
                print ('Все гласные', ex.h)
            else:
                print ('Все согласные', ex.t)
        if type(a) is int:
            a = str(a)
            for i in a:
                i = int(i)
                if i % 2 == 0:
                    self.ch += 1
                else:
                    self.nch += 1
            print('произведение суммы четных чисел на длинну числа', ex.ch * ex.func_1(a))
    def func_1(self, a):
        return len(str(a))


ex = Example()

c = input()
if c.isalpha():
    ex.func(c)
elif c.isdigit():
    ex.func(int(c))

# print('Гласные', ex.h, 'Согласные', ex.t)
# print('Четные', ex.ch, 'Не четные', ex.nch)
# print('Длинна', ex.func_1(c))