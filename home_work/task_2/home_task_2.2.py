from math import sqrt
x = float(input('введите значение'))
y = float(input('введите значение'))
r = float(input('введите радиус круга'))

h = sqrt(x**2 + y**2)

if h < r:
    print('точка в окружности')
else:
    print('точка вне окружности')