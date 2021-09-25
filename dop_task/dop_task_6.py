shcool = {'1a': ['Миша', 'Саша', 'Катя', 'Маша', 'Сергей'],
            '1b': ['Коля', 'Андрей', 'Игорь', 'Максим'],
            '2b': ['Женя', 'Толя', 'Оля', 'Яна'],
            '6a':['Надя', 'Толя', 'Саша'] }
print(shcool)
col = 0
col_w = []
key_l = []
del shcool['1b'][3]
shcool['7d'] = 'Женя', 'Толя', 'Оля', 'Яна'
del shcool['6a']
for val in shcool.values():
    col_w.append(len(val))
    col+=len(val)
for key in shcool.keys():
    key_l.append(key)
new_shcool = dict(zip(key_l,col_w))
sort_val = sorted(new_shcool.values())
sort_shcool = {}
for i in sort_val:
    for j in new_shcool:
        if new_shcool[j] == i:
            sort_shcool[j] = i
new_shcool_2 = {}
print(shcool)
print('оБЩЕЕ КОЛИЧЕСТВО учеников',col)
print(sort_shcool)
for i in sort_shcool:
    for j in shcool:
        if i == j:
            print((f"{i} - {shcool[i]}"))
