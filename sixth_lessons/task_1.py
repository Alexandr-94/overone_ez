import random

c = [random.randint(0,100) for i in range(10)]
c.append('task')            # дабавление в список
c.insert(1,'task_1')        # первая цифра место, вторая цифра элемент
c[3] = 'task_2'             # изменение элемента (после равно ставим элемент, в квадратных скобках индекс)
del c[2]                    # удаление элемента по индексу
c.remove('task')            # удаление указывая элемент
print(c)

print(c[0])
print(c[-1])
print(c[5])
print(c[-4])