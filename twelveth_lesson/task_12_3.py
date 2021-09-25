# t = open('two.txt', 'w')
# while True:
#     d = input('Введите текст')
#     if d =='':
#         break
#     t.write(d+'\n')
# t.close()

# f = open('two.txt')
# line = 0
# for i in f:
#     line += 1
#     print(i,len(i), 'символ.')
# print(line, 'стр.')
# f.close()

mas = ['world','hello', 1, 4, 3, 2, 'words','understand','Street']
w = []
g = []
print(mas)
s = str(mas)
for i in mas:
    if type(i) is str:
        w.append(i)
    else:
        g.append(i)
        g.sort()
h = sorted(w, key=len)
print(h)
print(g)
g_1 = str(g)
w_1 = str(w)
f = open('three.txt', 'w')
f.write(g_1+'\n'+w_1)
f.close()



