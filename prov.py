c_1 = (35,78,21,37,2,98,6,100,231)
c_2 = (45,21,124,76,5,23,91,234)
s_1 = sum(c_1)
s_2 = sum(c_2)

if s_1 > s_2:
    print('Сумма больше в кортеже - c_1',s_1)
elif s_1 < s_2:
    print('Сумма в кортеже больше - c_2',s_2)

print('Максимальное и минимальное значение кортежа c_1','максимальное -','Индекс -',c_1.index(max(c_1)), max(c_1),'Мигимальное -','Индекс -',c_1.index(min(c_1)), min(c_1))
print('Максимальное и минимальное значение кортежа c_2','максимальное -','Индекс -',c_2.index(max(c_2)), max(c_2),'Мигимальное -','Индекс -',c_2.index(min(c_2)), min(c_2))

string_1 = 'An apple a day keeps the doctor'
# str_2 =[]
# len_2 = []
# for i in string_1:
#     str_2.append(i)
#     len_1 = len(i)
#     len_2.append(len_1)
#     #print(len_1)
# dict_1 = dict (zip(str_2,len_2))
dict_1 = {d:string_1.count(d) for d in string_1}
print(dict_1)
#print(str_2)
#print(len_2)
#print(string_1)

list_1 = [1,2,3,4]
list_2 = [5,8,1,4]
list_3 = 0
for i in list_1:
    for j in list_2:
        if i == j:
            list_3+= i
print(list_3)
g = 0
p = 2
f = g / p
try:

    f = g / p
except ZeroDivisionError:
    print('деление на ноль')
finally:
    print('Гуд')


