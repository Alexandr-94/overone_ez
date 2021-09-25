import random

comp = ['Камень', 'Ножницы', 'Бумага']
# player = input('введите Камень, Ножницы или Бумага')
# print(player)
print('Увас есть 3 попытки!')
i = 1
while i <= 3:
    print(i)
    a = random.choice(comp)
    # print(a)
    player = input('введите Камень, Ножницы или Бумага')
    if a == 'Камень' and player == 'Камень' or a == 'Ножницы' and player == 'Ножницы' or a == 'Бумага' and player == 'Бумага':
        print(a)
        print('Ничья')
    elif a == 'Камень' and player == 'Бумага' or a == 'Бумага' and player == 'Ножницы' or a == 'Ножницы' and player == 'Камень':
        print(a)
        print('Игрок победил!')
    elif a == 'Ножницы' and player == 'Бумага' or a == 'Камень' and player == 'Ножницы' or a == 'Бумага' and player == 'Камень':
        print(a)
        print('Компьютер победил!')

    i += 1
# while i <= 3:
#     print(i)
#     player = input('введите Камень, Ножницы или Бумага')
#     if random.choice(comp) == 'Камень' and player == 'Камень' or random.choice(comp) =='Ножницы' and player == 'Ножницы'or random.choice(comp) =='Бумага' and player == 'Бумага':
#         print(random.choice(comp))
#         print('Ничья')
#
#     elif random.choice(comp) == 'Камень' and player == 'Бумага' or random.choice(comp) == 'Камень' and player == 'Ножницы' or random.choice(comp) == 'Ножницы' and player == 'Камень':
#         print(random.choice(comp))
#         print('Игрок победил!')
#
#     elif random.choice(comp) == 'Ножницы' and player == 'Бумага' or random.choice(comp) == 'Камень' and player == 'Ножницы' or random.choice(comp) == 'Бумага' and player == 'Камень':
#         print(random.choice(comp))
#         print('Компьютер победил!')
#
#     i +=1

