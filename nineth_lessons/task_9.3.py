# Words = dict()
# count = int(input('Количество слов в словаре'))
#
# i = 0
# while i<count:
#     print('Ввод слова')
#     wrd = str(input('Слово:'))
#     value = int(input('Значение:'))
#
#     if wrd not in Words:
#         Words[wrd] = value
#     i = i +1
# print(Words)

# Numbers = dict(zip([1,2,3], ['One', 'Two', 'Three']))
# print(Numbers)
a = 'pythonist'
d = {i:a.count(i) for i in a}
print(d)

