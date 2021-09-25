import random
a = random.randint(1, 10)
b = random.randint(1, 2)
i = 0

while i < 5:
    print(i)

    print(a)
    print(b)
    d = int(input('Введите число от 1 до 10 '))
    c = int(input('Введите число 1 или 2 '))
    if a == d and b == c:
        print('вы угадали!')
        break
    elif a!=d or b!=c:
        print('Числа не совпали попробуйте еще раз')
    i += 1
if i == 5:
    print('У вас закончилисть попытки, правильный ответ ', a,b)

