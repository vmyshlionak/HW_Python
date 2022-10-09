# 3.1. Дан список my_list = ['a', 'b', [1, 2, 3], 'd']. Распечатайте значения 1, 2, 3

# my_list = ['a', 'b', [1, 2, 3], 'd']
# list2 = my_list[2]
# print(list2)
# print(list2[0],',', list2[1] ,',',list2[2])

# 3.2 Дан список list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
#    - получите сумму всех чисел,
#    - распечатайте все строки, где есть буква 'a'

# list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
# sum_list = list(filter(lambda x : isinstance(x, int), list_1))
# print(sum_list)
# print(sum(sum_list))

# str_list = list(filter(lambda x : isinstance(x, str), list_1))
# for x in range (len(str_list)):
#  if 'a' in str_list[x]:
#   print(str_list[x])

#OR вместо for in
# print(list(filter(lambda x: 'a' in x, str_list)))

# Превратите лист ['cat', 'dog', 'horse, 'cow'] в кортеж

# my_list = ['cat', 'dog', 'horse', 'cow']
# new_tuple = tuple(my_list)
# print(new_tuple)

# 3.4. Напишите программу, которая определяет, какая семья больше.
#       1) Программа имеет два input() - например, family_1, family_2.
#       2) Членов семьи нужно перечислить через запятую.
#      Ожидаемый результат - программа выводит семью с бОльшим составом. Если состав одинаковый, print("Equal')

# family_1 = ['mother', 'father', 'daughter']
# family_2 = ['mother', 'son', 'grandmother', 'grandfather']
# if len(family_1) > len(family_2):
#  print(family_1)
# elif len(family_2) > len(family_1):
#  print(family_2)
# else:
#  print('Equal')

# Создайте словарь film c ключами title, director, year, budget, main_actor, slogan. В значения можете передать информацию
#     о вашем любимом фильме.
#     - распечатайте только ключи
#     - распечатайте только значения
#     - распечатайте пары ключ - значение

# equilibrium_dict = {'title':'Equilibrium', 'director': 'some guy', 'year': 2001, 'budget': 2000000,'main actor': 'Christian Bale',
#                     'slogan': 'The only thing more powerful than the system, is the man that will overthrow it. '}
# print(equilibrium_dict.keys())
# print(equilibrium_dict.values())
# new_tuple = equilibrium_dict.items()
# new_list = list(new_tuple)
# for x in range (len(new_list)):
#     print(new_list[x])

# Найдите сумму всех значений в словаре my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}

# my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
# print(sum(my_dictionary.values()))

# Удалите повторяющиеся значения из списка [1, 2, 3, 4, 5, 3, 2, 1]

# my_list = [1, 2, 3, 4, 5, 3, 2, 1]
# print(set(my_list))

# 3.8. Даны два множества: set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}, set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
#      - найдите значения, которые встречаются в обоих множествах
#      - найдите значения, которые не встречаются в обоих множествах
#      - проверьте являются ли эти множества подмножествами друг друга

# print(set1.issubset(set2))
# print(set2.issuperset(set1))
# print(set2.intersection(set1))
# print(set2.difference(set1))

# set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
# set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
# print(set1.intersection(set2))
# print(set1.difference(set2), set2.difference(set1))
# print(set1.issubset(set2))