import math
from math import *
from functools import *

# def sum1(a, b, c = 10):
#     return a + b + c
#
# print(sum1(2,3))

# def pattern(length, char1 = '~', char2 = '/'):
#     return (char1 + char2)*length
#
# print(pattern(10, '*'))

# scope (local, global)
# x = 35
# y = 25
# def sum_it(x, y):
#     print(locals()) #показывает локальные переменные функции
#     return x + y
#
# print(sum_it(5, 13))
# print(x+y) #сложит глобальные переменные

# lambda function

# f = lambda x,y: x*y
#
# print(f(5,6))
# print((lambda x, y: x*y)(5,8))

#Filter odd nums with custom function

# list_3 = [1, 2, 5, 8, 10, 105, 78]
#
# def take_odd(num):
#     if isinstance(num, int) and num%2:
#         return True
#     return False
#
# print(list(filter(take_odd, list_3))) # ну почему оно выдает числа, а не True, True, True??
# #OR
# odd_filtered = list(filter(lambda x: isinstance(x,int), list_3))
# print(list(filter(lambda x: x%2, odd_filtered)))

# modules

# from functools import reduce
#
# res = reduce(lambda x, y: x/y, [1, 2, 5, 6])
# print(res)

from my_calc import *

# def tests():
#     assert sum_it(11, 6) == 17, f'Actual result is {sum_it(11,6)}'
#     assert div(10,0) == "You can't divide by zero"
#     assert div(55,11) == 5, f'Actual result is {div(55,11)}'
#
# tests()

import datetime

# date_of_birth = 1982
# current_date = datetime.date.today()
# current_age = current_date.year - date_of_birth
# current_month = current_date.month

# print(current_age)
# print(current_month)
# print(current_date)

# list_1 = [2, 5 , 10]
#
# print(list(map(lambda x: x*x, list_1))) #map проходится по списку и совершает заданное действие с каждым элементом

# Homework
# 4.1. Напишите функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа):
#      периметр квадрата, площадь квадрата и диагональ квадрата.
#
# def square(x):
#     return (x*4, x*x, round(math.sqrt(x**2 + x**2)))
#
# print(square(5))

# 4.2. Напишите фукнцию, которая принимает произвольное количество именнованных аргументов и выводит их построчно
#      в формате аргумент: значение. Например:
# 	name: John
# 	last_name: Smith
# 	age: 35
# 	position: web developer

# def person(**kwargs):
#     for k, v in kwargs.items():
#         print(f'{k}: {v}')
#
# person(name = 'John', last_name = 'Smith', age = 35, position = 'QA')
#
# print(person(name = 'John', last_name = 'Smith', age = 35, position = 'QA'))
#
# 4.3. Используя лямбда-выражение, из списка my_list = [20, -3, 15, 2, -1, -21] создайте новый список, содержащий только
#      положительные числа

# my_list = [20, -3, 15, 2, -1, -21]
# print(list(filter(lambda x: x>=0, my_list)))

# 4.4. Используя лямбда выражение, получите результат перемножения значений в предыдущем списке

# print(reduce(lambda x, y: x*y, my_list))

# 4.5. Создайте файл my_calc.py и пропишите в нем минимум 4 функции, выполняющие базовые арифметические вычисления.
#      Примените эти функции в качестве методов в другом файле.

# print(sum_it(5,10))
# print(div(15,0))
# print(mult(20,4))
# print(minus_it(25, 65))