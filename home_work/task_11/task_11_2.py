# try:
#     a = input('число 1')
#     b = input('число 2')
#     с = int(a) / int(b)
# except ZeroDivisionError:
#     print('деление на ноль')
#
# else:
#     print(с**2)
#
# finally:
#     print('все гуд')

# while True:
#     a = input('число 1')
#     b = input('число 2')
#     try:
#         result = int(a)/int(b)
#     except ValueError:
#         print('Поддерживаются только числа')
#     except ZeroDivisionError:
#         print('на ноль делить нельзя')
#     else:
#         print(result)
#         break
dict = {'a':[1],'d':[1]}
try:
    print(dict['b'])
except KeyError:
    print('Такого кюча нет')
else:
    print('Нет такого словоря')
finally:
    print('все')
