import random

list = [random.randint(10,21) for i in range(10)]
print(list)

ind = list.index(20)
list[ind] = 200

print('изменённый список: \n', list)