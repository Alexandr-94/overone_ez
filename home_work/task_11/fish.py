import random


print('''Добрый день, вас преветствует менеджер по организации рыбалки''')

corm_and_fish = {'Червь':['Карась', 'Окунь', 'Лин', 'Красноперка'],
                 'Хлеб':['Карп', 'Лосось', 'Сазан', 'Плотва'],
                 'Опарыши':['Рыба-капля', 'Сом', 'Щука', 'Рыба-меч']
                }
ke = corm_and_fish.keys()
ke = list(ke)
val = corm_and_fish['Червь']
print(ke)
ul = []
ul_two = set(ul)


while True:
    print('пожалуйста наживки', ke)
    nazivka = str(input('выберите одну из наживок!'))
    i = 0
    #print(i)
    while i < 6:
        #print(i)
        #ch_corm_rand = random.choice(ke)
        #print(ch_corm_rand)
        if nazivka == ke[0]:
            one = random.choice(corm_and_fish['Червь'])
            ul.append(one)
            print(one)
        elif nazivka == ke[1]:
            two = random.choice(corm_and_fish['Хлеб'])
            ul.append(two)
            print(two)
        elif nazivka == ke[2]:
            thre = random.choice(corm_and_fish['Опарыши'])
            ul.append(thre)
            print(thre)
        else:
            print('вы ввели не правильную наживку')

        i += 1
    else:
        ul_two = set(ul)
        ul_three = list(ul_two)
        ul_one = ', '.join(ul_three)
        print('Ваш улов', ul_two)
        a = str(input('если вы больше не хотите рыбачить то напишите стоп, если желаете продолжить дальше введите любое значение'))
        if a == 'стоп':
            break
print('ваш улов я вас поздравляю! ',ul_one)
