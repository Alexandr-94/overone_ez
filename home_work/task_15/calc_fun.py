def plus(a,b):
    return a + b
def minus(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    try:
        return a / b
    except ZeroDivisionError:
        print('деление на ноль')

while True:
    a = float(input('введите число'))
    x = input('введите знак (+.-.*./) или если вы хотите выйти из програмы n ')
    if x == 'n':
        break
    b = float(input('введите число'))
    if x == "+":
        print(plus(a,b))
    elif x == "-":
        print(minus(a,b))
    elif x == "*":
        print(multiply(a,b))
    elif x == '/':
        print(divide(a,b))
        if x == '/' and a == 0 or b == 0:
            break
