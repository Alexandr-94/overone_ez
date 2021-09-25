a = input('введите текст')
print(a)
gl = ['a', 'e' , 'i', 'o', 'u', 'y']
app_gl = []
app_ngl = []
for i in a:
    if i in gl:
        print(i)
        app_gl.append(i)
    else:
        print(i)
        app_ngl.append(i)
print(len(app_gl), app_gl)
print(len(app_ngl), app_ngl)
d = len(app_gl)
c = len(app_ngl)
if d == c:
    print(app_gl)
else:
    print('не равны')

