a = float(input('введите число'))
b = input('операцию')
c = float(input('введите число'))
for i in range(0,10):
    if b == '+':
        print(a+c)
    elif b == '-':
        print(a-c)
    elif b == '/':
        print(a/c)
    elif b == '*':
        print(a*c)
    if b == 0:
        break
