a = 'Гладиолус,Чипсы,Огурец,Компьюте,Ноутбук'.split(',')

d = []
for i in a:
     d.append(len(i))

print('Самое длинное слово ',a[d.index(max(d))],',','состоит из',max(d),'символов')