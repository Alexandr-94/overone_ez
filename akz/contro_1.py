a = input('введите 7 число').split()
print(type(a),a)
ch = []
nh = []


for i in a:
    i = int(i)
    # print(i)
    if i % 2 == 0:
        ch.append(i)

    else:
        nh.append(i)
sm = 0
c = len(ch)
n = len(nh)
q = []

if c > n:
     print(sum(ch))
else:
    for i in a:
        i = int(i)
        q.append(i)
    sm = q[0] * q[2] * q[5]


print(q)
print(('произведение 1. 3 и 6 числа ='),sm)
print(('четные числа '),ch)
print(('не четные числа'),nh)



