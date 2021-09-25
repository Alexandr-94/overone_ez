# dict_1 = {'see': 'blak see',
#         'How many': 123}
#
# dict_1['Магазин'] = 34
# a = (1,2,3)
# b = [4,5,6]
# dict_1[a] = b
# print(dict_1)
# print(dict_1['see'])
# del dict_1['How many']
# print(dict_1)
# print(dict_1.keys())

# a = {'Саша','Сергей','Миша','Коля','Игорь'}
# b = {'Максим','Игорь','Саша','Надя','Катя','Сергей'}
# print(len(a),len(b))
# c=a|b
#
# print(c,len(c))
import random

# loto = dict(zip([1,2,3],['Александр', 'Миша', 'Сергей']))
# print(loto)
# print(len(loto.keys()))
# print(loto.values())
# print(random.choice(loto))

a = int(input('Кол-во уч'))
k = 0
i = set()
while k<a:
        c = input('Имя уч.')
        i.add(c)
        k += 0
w = 1
j = int(input())
while w <=j:
        m = i.pop()
        print('поб',w,'-',m)
        w+=1