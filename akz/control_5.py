# a = 'Ho123$35 8len'
# b = []
#
# for i in a:
#     if i in '1234567890':
#         b.append(i)
# print(b)
# print(b[0]+b[1]+b[2])
# print(b[3]+b[4])
# print(b[5])

a = input('введите строку')
b = ''
for i in a:
    if i.isdigit():
        b +=i
    elif b !='':
        print(b)
        b = ''
if b != '':
    print(b)