# Площадь полной поверхности рассчитывается по формуле: S = 2πr2 + 2πrh, r – радиус цилиндра, h – высота цилиндра
from math import pi
r = float(input('введите радиус целиндра'))
h = float(input('введите высоту целиндра'))
S = (2 * pi * r ** 2) + (2 * pi * r * h)
print(S)