x = float(input('введите число'))
y = 0

if x > 0:
    y = 2*x - 10
elif x == 0:
    y = 0
elif x < 0:
    y = 2*abs(x) - 1
print(y)
