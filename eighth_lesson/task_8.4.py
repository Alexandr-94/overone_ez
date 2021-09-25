import random

a = [random.randint(0,9)for i in range(10)]
a = tuple(a)
print(sum(a))
long_word = ('т','т','а','и','и','а','и','и','и','т','т','а','и','и','и','и','и','т','и')
print(long_word.count('т'),long_word.count('и'),long_word.count('а'))
week_temp = (26,29,34,32,28,26)
sum_temp = sum(week_temp)
days = len(week_temp)
mean_temp = sum_temp / days
print(days)
print(sum_temp)
print(int(mean_temp))