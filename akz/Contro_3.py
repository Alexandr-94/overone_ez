import random

i = 1
rond = 0
counter = 0

while i <= 7:
    print('число i', i)
    # if i ==7:
    #     break
    a = int(input('введите два число от 1 до 20'))
    d = int(input('введите два число от 1 до 20'))
    b = random.randint(1, 20)
    c = random.randint(1, 20)

    if a>b and d>c:
        counter += 1
    if a == b and d == c:
        rond += 1
    print('первое число введенное с клавиатуры',a)
    print('первое число введенное с клавиатуры',d)
    print('рандомное первое число',b)
    print('рандомное второе число',c)
    print('числа с клавиатуры были больше чем рандомные', counter)
    print('числа были равны ', rond)
    i+=1

