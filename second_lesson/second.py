x1 = float(input('введите число'))
y1 = float(input('вВЕДИТЕ ЧИСЛО'))
x2 = float(input('введите число'))
y2 = float(input('введите число'))

k = (y1-y2) / (x1-x2)
b = y2 - k * x2

print('\ty = %.2f+x + %.2f' % (k, b))
