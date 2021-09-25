my_list = ['hello','world']
elements = [1,3,my_list,6,'a','b']
print(elements)
del elements[2][1]
print(elements)
if 'hello' in elements [2]:
    print('yes.')


a = [1,3,5]
b = [1,5,8,9]

print(a+b)

d = ['h','e','l','l','o']
e = ['w','o','r','l','d']
d.extend(e)                 # extend не возвращает новый список, а дополняет текущий
print(d)



r = [1,2,3,4]
#t = r       # пременной t присваивается не значение списка r,t его адрес
t = r.copy()
a.append(5)
t.append(6)
print('r', r,'t',t)


# reverse=Tru