import random

a = [random.randint(0,5) for i in range(10)]
a = tuple(a)
b = [random.randint(-5,0) for i in range(10)]
b = tuple(b)
x = a + b
print(a)
print(b)
print(x)
print('количество нулей',x.count(0))