#калькулятор
a = float(input('введите число'))
b = input('введите символ')
c = float(input('введите число'))
if b == '+':
    print(a+c)
elif b == '-':
    print(a-c)
elif b == '*':
    print(a*c)
elif b == '/':
    print(a/c)
elif b != '+,-,*,/':
    print('таких знаков нет')
