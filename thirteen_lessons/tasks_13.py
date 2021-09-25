# def a_function():
#     print("You just created a function!")
#
# a_function()
#
# def empty_function():
#     pass
#
# def d_function():
#     d = [1, 2, 2, 2, 2, 3, 5, 5, 1, 6, 5]
#     print(sum(d))
# d_function()
#
# def add(a, b):
#     return a+b
# print(add(1, 2))
# print(add(a=2, b=3))
# total = add(b=4, a=5)
# print(total)

# def keyword_function(a=1, b=2):
#     return a+b
# print(keyword_function(b=4, a=5))
# print(keyword_function())

# def mixed_function(a, b=2, c=3):
#     return a + b + c
#
# mixed_function(1, b=4, c=5)
#
# print(mixed_function(1, b=4, c=5))
# print(mixed_function(1, 2, 3))

# def many(*args, **kwargs):
#     print(args)
#     print(kwargs)
# many(1, 2, 3, name='Mike', job='programmer')

# def function_a():
#     global a
#     a = 1
#     b = 2
#     return a + b
#
#
# def function_b():
#     c = 3
#     return a +c
#
# print(function_a())
# print(function_b())
#
# def func1(a, b):
#     def inner_func(x):
#         return x * x * x
#     return inner_func(a) + inner_func(b)
# print(func1(4, 5))
#
# def sum(a, b): return a + b
# print(sum(1, 5))

# def is_year_leap(a):
#
#     if a %4 ==0:
#         print('високосный')
#     else:
#         print('не високосный')
# is_year_leap(1339)

# def season(a):
#
#
#     if a == 1 or a == 2 or a == 11 or a == 12:
#         print('Зима')
#     elif a == 4 or a == 5 or a == 3:
#         print('Весна')
#     elif a == 6 or a == 7 or a == 8:
#         print('Лето')
#     elif a == 9 or a == 10:
#         print('Осень')
#     return a
# season(8)