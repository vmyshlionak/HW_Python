import time

import pyautogui

#FizzBuzz


# num = int(input("Enter a number from 1 to 10: "))

#решение c if else
# if num%3 == 0 and num%5:
#     print('Fizz')
# elif num%5 == 0 and num%3:
#     print('Buzz')
# elif num%3 == 0 and num%5 == 0:
#     print('FizzBuzz')
# else:
#     print(num)

#решение с циклом
#    i = i + 1

#Цикл для чисел фибоначчи

num1 = 0
num2 = 1
i = 0
print(num1)
print(num2)

while i < 10:
    fib_number = num1 + num2
    # num1 = num2
    # num2 = fib_number
    num1, num2 = num2, fib_number
    print(fib_number)
    i += 1

# n = 10
#
# for i in range (n):
#     fib_number = num1 + num2
#     num1 = num2
#     num2 = fib_number
#     print(fib_number)

# заставить нажиматься какую-то клавишу на клавиатуре каждые сколько-то секунд
# для этого была скачана и импортирована библиотека pyautogui, а также импортнула time модуль

# i = 1
# while i > 0:
#     pyautogui.press('numlock')
#     time.sleep(5)

#true если нечетное, false если четное и дробное
# def is_odd(n):
#     if n%2!=0 and n%1==0:
#         return True
#     else:
#         return False

sentence = 'I love you'
# print(list(sentence))

#or

# my_list = sentence.split(' ')
# print(my_list)
# my_list.append('not')
# print(my_list)
# print(my_list.index('love'))
# my_list = sentence
# my_list1 = 'not'
# # my_list.extend(my_list1)
# print(my_list[2:])#вывести весь список, начиная с третьего элемента и до последнего включительно

# list comprehension

# l = [1, 2, 3, 4, 5]
# new_list = [x*x for x in l if x%2==0]# создаем новый список, совершая операции над элементами старого (возводим в степень четные)
# print(new_list)

# dictionaries

my_smth = {'name':'Vika', 'last name':'Myshlionok'}
print(my_smth.items())
