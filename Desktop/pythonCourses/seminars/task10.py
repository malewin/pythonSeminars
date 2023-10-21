# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
#  решкой, а некоторые – гербом. Определите минимальное число
#  монеток, которые нужно перевернуть, чтобы все монетки были
#  повернуты вверх одной и той же стороной. Выведите минимальное
#  количество монет, которые нужно перевернуть.
#  5 -> 1 0 1 1 0 2

from random import randint # необходим модуль для функции рандомного заполнения
n = int(input('enter an amount of coins: ')) # количество монет введённое пользователем

def autofill(amount): # метод автозаполнения массива элементами: 0 и 1
    list_comprehension = [randint(0,1) for i in range(abs(amount))] # взял по модулю на случай если клиент введёт значение < 0
    return list_comprehension

def whatBiggerAndHowMuch (list): # метод определения сколько решек и орлов, какие переворачивать
    count0 = 0
    count1 = 0
    for i in list:
        if list[i] == 0:
            count0 += 1
        else:
            count1 += 1
    if count0 > count1:
        res = count1
    else:
        res = count0
    print(f'на столе лежат стороной вверх: \n{count0} монет - решкой, \n{count1} монет - гербом')
    print(f'{res} минимальное кол-во монет которое нужно перевернуть, чтобы все лежали одной стороной')

# print(autofill(n))

whatBiggerAndHowMuch(autofill(n))








