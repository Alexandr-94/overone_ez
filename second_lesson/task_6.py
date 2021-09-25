a = float(input())
b = float(input())
c = float(input())

v = a + b > c
d = b + c > a
h = c + a > b

if v or d or h:
    print('треугольник существует')