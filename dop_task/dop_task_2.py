a = input('Введите трех значное число')
f = []
# n = a // 10 % 10
# b = a % 10
# a = a // 100
# c = a + b + n
# print(c)
# print(a)
# print(n)
# print(b)

for i in a:
    i = int(i)
    f.append(i)
c = sum(f)
print(f)
print(c)