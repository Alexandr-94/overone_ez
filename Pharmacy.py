import random, math

# Ключи - симптомы; значение - словари где ключ - препарат, значение - список [кол-во пластинок в пачке, таблеток в пачке, пачек на складе, цена]
drugs = {
    'простуда': {
        'аугментин': [2, 14, 11, 21.40],
        'терафлю': [10, 10, 23.7, 23.2],
        'ибуфен': [2, 20, 30.5, 7]
                },
    'расстройство': {
        'стопдиар': [1, 24, 100, 7.61],
        'смекта' : [10, 10, 55, 10.8]
    },
    'изжога': {
        'нельпаза': [1, 14, 66, 9.71],
        'ренни': [2, 24, 48, 10.6]
    },
    'давление': {
        'диротон': [2, 28, 45, 7],
        'панангин': [1, 50, 77, 11]
    },
    'аллергия':{
        'эриус':[1, 10, 12, 34.8],
        'аквамарис': [1, 1, 56, 12,33]
    },
    'боль в горле':{
        'грамидин': [1, 18, 25, 17.64],
        'тантум верде': [1, 1, 8, 20.82]
    },
    'боль': {
        'спазмалгон': [1, 24, 11, 10.82],
        'ношпа' : [1, 24, 11, 11.51]
    },
    'кашель': {
        'ренгалин': [2, 20, 11, 9.56],
        'гербион': [1, 1, 44, 14.71]
    }
}
print('Привестствуем вас в нашей онлайн - аптеке!\n')
prescribing = '' #Тут хранится название препарата
bill = 0 #цена ИТОГО
final_drugs = [] #Массив для чека, там хранятся названия препаратов
final_piils_numb = [] #Тут хранится к-во купленного
final_price = [] #тут хранятся цены купленного
symp = '' #Сюда покупатель вводит симптомы
while symp != 'Всё':
    symp = input(
        f'Введите ваш симптом что б мы могли вам помочь!\nДля окончания покупок просто наберите "Всё" вместо симптома.\nПока что мы работаем только с симптомами: {", ".join(list(drugs.keys()))}\n')
    if symp in drugs:
        prescribing = random.choice(list(drugs[symp].keys())) # рандомно выбираем один из препаратов по симптому
        pills_blister = drugs[symp][prescribing][1]/drugs[symp][prescribing][0] # таблеток в блистере
        blister_price = drugs[symp][prescribing][3]/drugs[symp][prescribing][0] # цена блистера
        if drugs[symp][prescribing][0] == 1 and drugs[symp][prescribing][1] == 1: # если количество блистеров и талеток в пачке = 1, то это либо сироп либо капли  и т.д.
            print(f'При вашем симптоме "{symp}" отлично помогает {prescribing},\nцена: {drugs[symp][prescribing][3]} за 1 флакон')
            final_drugs.append(prescribing) # Добавляем название препарата в чек
            pills_numb = int(input('Сколько флаконов вам надо?\n')) # Тут хранится сколько покупатель хочет купить
            if pills_numb <= drugs[symp][prescribing][2]:
                bill += drugs[symp][prescribing][3]*pills_numb # суммируем итого
                final_piils_numb.append(pills_numb) # добавляем количество купленного
                final_price.append(pills_numb*drugs[symp][prescribing][3]) # добавляем цену в чек
                drugs[symp][prescribing][2] = drugs[symp][prescribing][2] - pills_numb #Здесь убираем купленное со склада
            else:
                print(f'К сожалению столько нет, добавили вам в чек вот столько - {drugs[symp][prescribing][2]}') # если покупатель хочет больше чем у нас есть, то продаем всё что есть
                bill += drugs[symp][prescribing][2]*drugs[symp][prescribing][3]
                final_piils_numb.append(drugs[symp][prescribing][2])
                final_price.append(drugs[symp][prescribing][2] * drugs[symp][prescribing][3])
                drugs[symp][prescribing][2] = 0 #Здесь убираем купленное со склада
        elif drugs[symp][prescribing][0] == 1 and drugs[symp][prescribing][1] != 1: # если количество блистеров 1, а атблеток в пачке != 1 то значит купить можно только по пачкам.
            print(f'При вашем симптоме "{symp}" отлично помогает {prescribing},\nв одной пачке {drugs[symp][prescribing][1]} таблеток,\nцена: {drugs[symp][prescribing][3]}')
            pills_numb = int(input('Сколько пачек вам надо?\n'))  # Тут хранится сколько покупатель хочет купить
            final_drugs.append(prescribing)
            if pills_numb <= drugs[symp][prescribing][2]:
                bill += drugs[symp][prescribing][3]*pills_numb
                final_piils_numb.append(pills_numb)
                final_price.append(drugs[symp][prescribing][3]*pills_numb)
                drugs[symp][prescribing][2] = drugs[symp][prescribing][2] - pills_numb
            else:
                print(f'К сожалению столько нет, добавили вам в чек вот столько - {drugs[symp][prescribing][2]}')
                bill += drugs[symp][prescribing][2]*drugs[symp][prescribing][3]
                final_piils_numb.append(drugs[symp][prescribing][2])
                final_price.append(drugs[symp][prescribing][2]*drugs[symp][prescribing][3])
                drugs[symp][prescribing][2] = 0
        else: # В этом случае можно купить по блистерам.
            print(f'При вашем симптоме "{symp}" отлично помогает {prescribing},\nв одной пачке {drugs[symp][prescribing][1]} таблеток в {drugs[symp][prescribing][0]} блистерах,\n'
                  f'цена за пачку: {drugs[symp][prescribing][3]}')
            pills_numb = int(input('Сколько таблеток вам надо?\n'))
            if pills_numb < drugs[symp][prescribing][2]*drugs[symp][prescribing][1]: # Проверяем кол-во таблеток на складе, на складе всё хранится в пачках.
                if pills_numb == drugs[symp][prescribing][1]:
                    bill += drugs[symp][prescribing][3]
                    final_piils_numb.append(1)
                    final_price.append(drugs[symp][prescribing][3])
                else:
                    # количество заказынных таблеток / на к-во таблеток в блистере, окргуляем вверх и умножаем на цену блистера
                    bill += math.ceil(pills_numb/pills_blister)*blister_price
                    final_drugs.append(prescribing)
                    final_piils_numb.append(math.ceil(pills_numb/pills_blister)/drugs[symp][prescribing][0])
                    final_price.append(math.ceil(pills_numb/pills_blister)*blister_price)
    elif symp not in drugs and symp != 'Всё':
        print(f'К сожалению симптома "{symp}" пока нет в нашей аптеке, наберите симптом из списка либо закончите работу.')
        continue
print('     ОАО "Болей еще!"')
for i in final_drugs:
    print(f'\n{i}\t{final_piils_numb[final_drugs.index(i)]}\t{final_price[final_drugs.index(i)]}')
print(f'Итого : {bill} р.')