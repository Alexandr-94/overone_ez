# n = int(input('Ведите трехзначное число: '))        # если брать в пример цифру 349
#
# a = n % 10              # остаток от деления n на 10 (34.9 остаток 9)
# n = n // 10             # делем n на целое на 10 (34)
# b = n % 10              # остаток от n на 10 (3.4 остаток 4)
# c = n // 10             # делем n на целое на 10 (3.4 целое 3)
#
# print('Сумма цифр трехзначного числа', c + a + b)       # сумма цифр 16


import random
import time
bread = ['Карась на 400гр', 'Плотва на 100гр', 'Краснопёрка на 120гр']
worms = ['Карась на 600гр', 'Карп на 800гр', 'Линь на 300гр']
bloodworm = ['Линь на 500', 'Ротан на 90', 'Лещ на 600']
print('Здравствуйте уважаемый любитель или профессиональный рыболов! \n'
      'Мы приветствуем вас на нашем водоёме "Красулино"!')
print()
time.sleep(4)
print('Вам можно ловить не дольше 3х часов! \n'
      'У нас есть Карась, Плотва, Краснопёрка, Карп, Линь, Лещ, Ротан')
print()
time.sleep(4)
def chosenBait():
    print('Выберите какой приманкой будете ловить: хлеб, черви, мотыль.')
    bait = input()
    print('Вы поймали ....')
    time.sleep(2)
    cage = set()
    for i in range (3):
        if bait == 'Хлеб' or bait == 'хлеб' or bait=='ХЛЕБ':
            cage.add(random.choice(bread))
        elif bait == 'мотыль' or bait =='Мотыль' or bait =='МОТЫЛЬ':
            cage.add(random.choice(bloodworm))
        elif bait == 'черви' or bait =='Черви' or bait =='ЧЕРВИ':
            cage.add(random.choice(worms))
        else:
            print('Введите ПРАВИЛЬНО название приманки')
        if i == 0:
            print("За 1ый час .... ")
            print(cage)
        elif i ==1 :
            print("За 2ой час .... ")
            print(cage)
        if i == 2:
            print("За 3ий час ....")
            print(cage)
fishingAgaing = 'да'
while fishingAgaing == 'да' or fishingAgaing == 'ДА':
    chosenBait()
    print('Попробуете половить ещё за отдельную плату ? =)')
    fishingAgaing = input()