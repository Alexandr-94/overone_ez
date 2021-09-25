# products = {'Хлеб': [2.5, 25,],            # магазин
#             'Сосиски': [5, 10],
#             'Сахор': [1.5, 5],
#             'Мука': [3, 26],
#             'Масло': [1, 4],
#             }
# print(products)
# list_ch = []
# list_ne = []
# ch =input(('введите продукты из списка')).split(' ')
# #value_1 = int(input('введите количество'))
# #ch_1 = ''.join(ch)
# #print(ch)
# #print(type(ch_1))
# for key in ch:
#     if key in products:
#         list_ne.append(key)
#         list_ch.append(products[key][0])
#         print(key)
# print('Покупка на сумму',sum(list_ch),'$')
#
# # Сосиски Мука Масло Хлеб


goods = {'apple':[4.5, 10],
         'orenge':[6.2, 5],
         'pineapple':[10.0, 1],
         'mango':[7.5, 2],
         'banana':[3.8,10]}

for key, value in goods.items():
    print(key, '-', value[0], '-', value[1])
cost = 0
while True:
    good = input('What? (n - nothing)')
    if good == 'n' or good not in goods.keys():
        break
    qty = int(input('How many? '))
    if qty > goods[good][1]:
        print("We don't have so much.")
        continue
    cost += goods[good][0] * qty
    goods[good][1] -= qty
print('Price:', cost)
print('__________________________')
for key, value in goods.items():
    print(key, '-', value[0], '-', value[1])