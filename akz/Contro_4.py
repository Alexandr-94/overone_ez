import random
k = 0
a = int(input('введите количество чисел максимум до 30'))
print('кколичество чисел',a)
b = int(input('введите число которое надо найти'))
c = [random.randint(0,30) for i in range(a)]
for i in c:
    if b in i:
        k += 1


print('число которое надо найти',b)
print('рандомный список чисел', c)