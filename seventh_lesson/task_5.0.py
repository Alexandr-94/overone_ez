# 1 задача
# import math
# a = int(input())
# b = int(input())
# c = math.sqrt(a ** 2 + b ** 2)
# print(f'гипотенуза ,{c}')
# 2 задача
a = int(input())
b = int(input())
c = int(input())

if a < b < c or c < b < a:
    print(b)
elif b < a < c or c < a < b:
    print(a)
else:
    print(c)

#3 задача










#4 задача

# a = int(input('введите многозначное число'))
# b = 0
# while a >0:
#     b = b * 10 + a % 10
#     a = a // 10
# print(b)

#5 задача
# c = input('контур')
# b = input('центр')
# dl = int(input('Длинна'))
# sh = int(input('высота'))
# i = 0
# while i <= sh:
#     if i == 0 or i == sh:
#         print(c * dl)
#     else:
#         print(c + b * (dl - 2) + c)
#     i = i + 1
# print(sh*c)
# for i in range(dl - 2):
#     #print(c + b * (sh-2) + c)
#     print(f'{c}{b*(sh-2)}{c}')
# print(sh*c)

# 6 задача
# for i in range(2,10001):
#     d = 0
#     for j in range(1,int(i//2)+1):
#         if i % j == 0:
#             d += j
#     if d == i:
#         print(d)
#
# 7 задание

# arr = []
# a = int(input('сколько элементов'))
# for i in range(a):
#     j = int(input())
#     arr.append(i)
# b = int(input(''))
# c = int(input(''))
# arr.insert(c,b)
# print(arr)

# 7 задание
# a = str(input('введите три слова через пробел'))
# c = a.count(' ')
# c += 1
# s = a.split()
# print(len(s))

#8 задание

# a = input('введите строку')
# c = ''
# for i in a:
#     if i.islower():
#         c += i
# print(c)

#9 задание


