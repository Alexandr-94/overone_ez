a = float(input('введите число'))
b = input('операцию')
c = float(input('введите число'))
while True:
    if c == 0:
        print("операция равна нулю")
        break
    elif b == '+':
        print(a+c)
    elif b == '-':
        print(a-c)
    elif b == '/':
        print(a/c)
    elif b == '*':
        print(a*c)
    elif c == 0:
        break