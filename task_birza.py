import random

convert = { # Конверсия
    'usd': 0.8,
    'eur': 1.2
}
user_money = { # Стартовый капитал
    'usd': 500,
    'eur': 500
}
print(f'Ваш стартовый портфель: usd -  {user_money["usd"]}, eur - {user_money["eur"]}, всего 900 eur')
t = 0
currency_change = 0 # Изменения в курсе конверсии
user_action = '' # Действия пользователя
while t <= 1:
    for i in convert: # Здесь меняем курс конверсии каждой валюты на случайную величину
        currency_change = round(random.uniform(-0.2, 0.2), 3)
        convert[i] = convert[i] + currency_change
        sign = '' # Только для красивого выводв положительнх и отрицательных изменений
        if currency_change > 0:
            sign = '+'
        print(f'Изменения курса {i}: {sign}{currency_change}') # Ну собственно сам вывод
        # здесь пользователь вводит что он будет делать
    user_action = input(
        # B - buy - покупать, S - sell - продавать
        'Введите валюту, через пробел B - для покупки либо S - для продажи и далее через пробел количество').split()
    if user_action[1] == 'B': # Если покупаем то отнимаем сумму на которую покупаем, переводим её в валюту которую покупаем
        if user_action[0] == 'usd': # и добавляем к имеющейся
            user_money['usd'] = user_money['usd'] + int(user_action[2])
            user_money['eur'] = round(user_money['eur'] - (int(user_action[2]) * convert['usd']), 3)
        elif user_action[0] == 'eur':
            user_money['eur'] = user_money['eur'] + int(user_action[2])
            user_money['usd'] = round(user_money['usd'] - (int(user_action[2]) * convert['eur']), 3)
    elif user_action[1] == 'S': # Если продаем то отнимаем сумму которую продаём переводим в дургую валюту и прибавляем
        if user_action[0] == 'usd':
            user_money['usd'] = user_money['usd'] - int(user_action[2])
            user_money['eur'] = round(user_money['eur'] + (int(user_action[2]) * convert['usd']), 3)
        elif user_action[0] == 'eur':
            user_money['eur'] = user_money['eur'] - int(user_action[2])
            user_money['usd'] = round(user_money['usd'] + (int(user_action[2]) * convert['eur']), 3)
    print('Ваши деньги')
    for i in user_money: # После каждой операции показывает капитал пользователся
        print(f'{i} - {user_money[i]}')
    t += 1 # Счётчик
result = round(user_money['usd'] * convert['usd'] + user_money['eur'], 3) # Для расчёта профита
profit = ''
if result > 900: # Для расчёта профита
    profit = round(result - 900, 3)
else:
    profit = round(900 - result, 3)
print( # ИТОГО
    f'Итого:\nБыло: usd - 500, eur - 500\nСтало:usd - {user_money["usd"]}, eur - {user_money["eur"]}\nПрофит - {profit} eur')
