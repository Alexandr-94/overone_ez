# def factorial(n):
#     if n != 0:
#         return n * factorial(n - 1)
#     else:
#         return 1
# print(factorial(5))
#
# product = lambda x, y: x * y
# print(product(2,3))
#
# def mul(a):
#     def helper(b):
#         return a * b
#     return helper
# print(mul(3)(2))
# def simple_decore(fn):
#     print('Start function')
#     fn()
#     print('Stop function')
# @simple_decore
# def first_test():
#     print('Test function 1')
# @simple_decore
# def second_test():
#     print('Test function 2')


# first_test_wrapperd = simple_decore(first_test)
# second_test_wrapperd = simple_decore(second_test)

# def o(x):
#     i = 0
#     while x>0:
#         i +=1
#         x = x//10
#     return i
#
# print(o(123))
# import math
# from math import pi
#
#
#
# def plo_cirkl():
#     r = int(input('радиус'))
#     s = pi * r
#     return s
# def plo_pr():
#     a = int(input('введите первое значение'))
#     b = int(input('введите второе значение'))
#     s_1 = a * b
#     return s_1
# def plo_treu():
#     a = int(input(''))
#     b= int(input(''))
#     c= int(input(''))
#     s = (a+b+c)/2
#     return math.sqrt(s(s-a)(s-b)(s-c))
# print(plo_treu())
import random

#
# def rand():
#     a = int(input('от'))
#     b = int(input('до'))
#     s = ([random.randint (a,b) for i in range(10)])
#     print(s)
# rand()
#
#
# N = 10
# a = [0] * N
#
# def func(mn, mx):
#     for i in range(N):
#         a[i] = random.randint(mn, mx)
# mn = int(input('начало'))
# mx = int(input('Конец'))
#func(mn, mx)
#print(a)
# teme_1 = 1234565
# def teme():
#     d = teme_1 // 86400
#     h = (teme_1%86400)//3600
#     return d, h
# print(teme())
# a = 'aoieu'
# gl = 0
# sg = 0
# def gl_1(str_1):
#    for i in str_1:
#       gl += 1
#
#    else:
#        sg += 1
# print(gl_1)

# def o(n):
#     return int(str(n) + str(n*2) + str(n*3))
# print(o(1))
