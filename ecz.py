# l = []
# for i in l:
#     if l.count(i) == 1:
#         print(i)
# l = [1, 2, 2, 3, 1, 2, 5, 2]
# f = 0
# for i in l:
#     if l.count(i) > 1:
#         f += 1
# print(f//2)

# s = 'python, JS! C?'
# signs = ',!?.%$'
# q = ''
# print(s)
# for i in s:
#     if i not in signs:
#         q = q+i
# print(q)

# candy_shop = {
#     'cake': ['milk sugar', 2, 1000],
#     'muffin': ['sugar flavour', 30, 500],
#     'donut': ['sugar peanut butter', 5, 20]
# }
# for i in list(candy_shop.keys()):
#     print(i)
# while True:
#     a = input('what do you want?')
#     if a == '1':
#         for i in candy_shop:
#             print(i, candy_shop[i][0])
#     if a == '2':
#         for i in candy_shop:
#             print(i, candy_shop[i][1])
#     if a == '3':
#         for i in candy_shop:
#             print(i, candy_shop[i][2])
#     if a == '4':
#         for i in candy_shop:
#             print(i, str(candy_shop[i]))
#     if a == '5':
#         price = 0
#         while True:
#             b = input('type here what you want')
#
#             if b == 'n':
#                 break
#             elif b in candy_shop:
#                 b2 = int(input('how much'))
#                 candy_shop[b][2]= candy_shop[b][2]-b2
#                 price = b2*candy_shop[b][1]
#
#     elif a == '6':
#         print('bye')
#         break
#
# print(candy_shop)
# print(price)
# with open('class.txt') as c:
#     d = []
#     s = c.readlines()
#     z = 0
#     for i in s:
#         i = i[:-1]
#         if int(i[-1]) < 3:
#             print(i)
#         z = z + int(i[-1])
# print(z / len(s))
# with open('class.txt', encoding='UTF-8') as c:
#     s = c.readlines()
#     a= []
#     people = {}
#     for i in s:
#         if i != '':
#             people[(i[:-1]).split(':')[0]] = (i[:-1]).split(':')[1:]
#     l = list(sorted(people.keys()))
#     for i in people: # 1
#         print(i, people[i])
#     x = input('find')
#     if x in people: # 4
#         print(x, people[x])
#     people[input()] = [input(), input()] # 5
us=500
eu=500
kursconv=0.81
teu=eu
tus=us
tempeu=us*kursconv
tempeu1=eu+tempeu
import random
while (True):
     kursconv=random.uniform(0.7,1)
     kursconvus=random.uniform(1.2,1.6)
     print(kursconv)
     p=input('Вы хотите купить или продать валюту? ')
     # if p!='купить' or p!='продать':
     #     break
     p1=input('какую валюту eu/us ')
     p2=int(input('сколько? '))
     if p=='купить':
         if p1=='eu':
             eu1=p2*kursconv
             us=us-p2
             eu=eu+eu1
             print(eu,us)
         else:
              us1=p2*kursconvus
              eu=eu-p2
              us=us+us1
              print(us,eu)
     elif p=='продать':
         if p1 == 'eu':
             us1 = p2 * kursconvus
             eu = eu - p2
             us = us + us1
             print(us, eu)
         else:
             eu1 = p2 * kursconv
             us = us - p2
             eu = eu + eu1
             print(eu, us)
         if p!='купить' or p!='продать':
            break

