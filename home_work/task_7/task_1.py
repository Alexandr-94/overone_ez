list = [15, 48, 'hello', 6, 19, 'world']
print(list)
ch = []
gl = ['a', 'e' , 'i', 'o', 'u', 'y']

app_gl = []
app_ngl = []
for i in list:
    if type(i) is int:
        if i%2 == 0:
            d = i % 10
            ch.append(d)
            c = i //10
            ch.append(c)

        else:
            list[list.index(i)] = 1
    if type(i) is str:

        for i in i:
            if i in gl:
                #print(i)
                app_gl.append(app_gl)
            else:
                #print(i)
                app_ngl.append(app_ngl)
        #print(type(i))

print('глассные',len(app_gl))
print('cогласные', len(app_ngl))
print('замена нечетных чисел на 1',list)
print('сумма четных чисел',sum(ch))
