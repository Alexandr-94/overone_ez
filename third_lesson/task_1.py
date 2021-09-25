a = float(input('введите число'))
b = float(input('введите число'))
с = float(input('введите число'))

if a % 10 == 0 or b % 10 == 0:
    if a + b > c and b + c > a and c + a > b:
        print('треугольник существует')
    else:
        print('треугольника нет')
else:
    if a % 2 == 0 and b % 2 == 0:
        print('четное')
    else:
        b = a**2
        print(b)