# найти уровнение y = kx + b
print('A(x1; y1):')
x1 = float(input('\tx = '))
y1 = float(input('\ty = '))

print('B(x2; y2):')
x2 = float(input('\tx2 = '))
y2 = float(input('\ty2 = '))

print('Equation:')
k = (y1 - y2) / (x1 - x2)
b = y2 - k * x2
print('\ty = %.2f*x + %.2f' % (k,b))
