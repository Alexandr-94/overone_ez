
products = {'Bread': [2.5, 25,],            # магазин
            'Sausages': [5, 10],
            'Sugar': [1.5, 5],
            'Vegetables': [3, 26],
            'Butter': [1, 4],
            }
print(products)
choose = dict()                                                         # список покупателя
print('What would you want choose?', products.keys())
please = int(input('Please enter quantity of products'))                # количество продуктов которые хочет купить клиент
#want = input('Please enter what you want to buy from the list above')
ch = 0
while ch < please:
    print(please)
    print(ch)
    products_1 = str(input('Please enter what you want to buy from the list above, please enter of one products'))  # название продукта так же его ключ в словаре
    value_1 = int(input('Please enter quantity of products'))             # количество продуктов (шт)
    #print(products_1, ':', value_1)

    if products_1 not in choose:                # проверяем есть ли в словоре значение
        #print('this product is not, pleas enter product from the list above')
        choose[products_1] = value_1              # добавляем ключ и количество
    ch = ch + 1

p_k = products.keys()
for key in choose:
    if key in products:
        print(key)
    elif


                          # ключ словаря products
# p_ck = choose.keys()                            # ключ словаря choose
# print('ключи',p_k,p_ck)
#print(choose)

                                                # не могу понять как бы мне сравнить два словаря products and chose
                                                # что бы то что есть в choose  вывести в новой переменной типо чека где будет указан продукт стоимость
                                                # кол-во. а в products  отнялось количество !!!????)))
                                                # I need your Help, please!!))