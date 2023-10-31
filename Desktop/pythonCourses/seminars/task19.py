#  Задача No19. Решение в группах
# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо, K – положительное число.
# Input: [1, 2, 3, 4, 5] k = 3 Output: [4, 5, 1, 2, 3]
# Примечание: Пользователь может вводить значения списка или список задан изначально.

from random import randint # необходим модуль для функции рандомного заполнения
x = int(input('сколько чисел в вашем списке?: ')) # количество элементов в рандомном списке
minRandBorder = int(input('какое минимальное значение элемента в диапазоне элементов вашего рандомного списка чисел?: ')) # минимум диапазона значений в списке
maxRandBorder = int(input('какое максимальное значение элемента в диапазоне элементов вашего рандомного списка чисел?: ')) # максимум диапазона значений в списке
n = int(input('на сколько индексов вправо сдвигаем наши элементы?: '))
listOfDiffValue = [] # создаем список для автозаполнения


def correctInput(amountOfElements , step):
    while (step >= amountOfElements):
        step = int(input('на сколько индексов вправо сдвигаем наши элементы?: '))
    return step

def autofill(amount, minBorder, maxBorder): # метод автозаполнения массива элементами: от min до maz
    list_comprehension = [randint(minBorder,maxBorder) for i in range(abs(amount))] # взял по модулю на случай если клиент введёт значение < 0
    return list_comprehension


correctInput(x, n)
listOfDiffValue = autofill(x, minRandBorder, maxRandBorder)
print(f'Ваш изначальный список: {listOfDiffValue}')
for i in range(n):              # алгоритмически с помощью цикла
    temp = listOfDiffValue.pop()
    listOfDiffValue.insert(0, temp)
print(f'Ваш свиднутый список на {n} элементов вправо: {listOfDiffValue}')

# с помощью срезов

# resultList = listOfDiffValue[-n:] + listOfDiffValue[:-n]
# print(f'Ваш свиднутый список на {n} элементов вправо: {resultList}')

