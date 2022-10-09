
# Напишите программу, которая проверяет здоровье персонажа в игре.
# Если оно равно или меньше нуля, выведите на экран False, в противном случае True.

# player_health = int(input("Enter player health: "))
#
# if player_health <= 0:
#     print (False)
# else:
#     print (True)

# Напишите программу, которая проверяет является ли введенное число четным.
# Если да, выведите на экран текст “Четное”, а иначе - “Нечетное”

# num = int(input("Enter a number: "))
#
# if num%2 == 0:
#     print ("Even")
# else:
#     print("Odd")
# #or
#
# if num%2:
#     print('Odd') #то есть когда остаток есть (True)
# else:
#     print('Even')

# Напишите программу, которая проверяет является ли год високосным.
# Таковыми считаются года, которые делятся без остатка на 4 (2004, 2008)
# и не являются столетиями (500, 600). Однако, если год делится без остатка
# на 400, он также считается високосным (1200, 2000)

# year = 13
#
# if year%400 == 0:
#     print("Leap")
# elif(year%4 == 0 and year%100 != 0):
#     print("Leap")
# else:
#     print("Not leap")

# if year%4 == 0 and year%100 != 0:
#     print("Leap")
# elif year%400 == 0:
#     print("Leap")
# else:
#     print("Not leap")


# Напишите программу, которая печатает введенный текст заданное количество раз, построчно.
# Текст и количество повторений нужно ввести с помощью input()

# text = input("Enter some text: ")
# number_of_prints = int(input("How many times do you want to print your text? "))

# решение без циклов
# print((text+ "\n")*number_of_prints)

#решение через while
# x = 1
# while x <= number_of_prints:
#     print(text)
#     x += 1

#решение через for
# for i in range(number_of_prints):
#     print (text)

#вывод индексов букс стринга (начиная с 0)
# word = "Danila"
# for i in range(len(word)):
#     print(i)

