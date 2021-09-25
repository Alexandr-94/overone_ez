while True:
    try:
        a = input('Введите сначала числа, во во второй итерации числа')
        b = input('Введите сначала числа, во во второй итерации числа')
        c = int(a) / int(b)

    except ZeroDivisionError:
        print('вы делите на ноль, введите числа занова')
        continue
    except ValueError:
        print('Вы ввели бучкы')
    else:
        print(c)
        d = input('Если не жедлаете больше пробовать вводить данные то введите слово. stop')
        if d in 'stop':
            break




