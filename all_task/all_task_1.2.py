# вводят три целых числа, какое из них наибольшее.
a = int(input('введите целое число'))
b = int(input('введите целое число'))
c = int(input('введите целое число'))

if a < b > c:
    print('Больше', b)
elif b < a > c:
    print('Больше', a)
elif b < c > a:
    print('Больше', c)
else:
    print('все ровны')