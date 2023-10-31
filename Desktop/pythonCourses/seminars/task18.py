# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
#       5
# 1234 5
# 6
# -> 5

from random import randint # необходим модуль для функции рандомного заполнения
n = int(input('сколько чисел в вашем списке?: ')) # количество элементов в рандомном списке
minRandBorder = int(input('какое минимальное значение элемента в диапазоне элементов вашего рандомного списка чисел?: ')) # минимум диапазона значений в списке
maxRandBorder = int(input('какое максимальное значение элемента в диапазоне элементов вашего рандомного списка чисел?: ')) # максимум диапазона значений в списке
x = int(input('какое значение парсим?: '))
listOfDiffValue = [] # создаем список для автозаполнения

def autofill(amount, minBorder, maxBorder): # метод автозаполнения массива элементами: от min до max
    list_comprehension = [randint(minBorder,maxBorder) for i in range(abs(amount))] # взял по модулю на случай если клиент введёт значение < 0
    return list_comprehension

listOfDiffValue = autofill(n, minRandBorder, maxRandBorder)
print(f'Ваш изначальный список: {listOfDiffValue}')

def parsing(userList, x):
    min = abs(i-x)
    temp1 = abs(userList(i+1) - x)
    for i in userList:
        if min < temp1:
            return i
        else
