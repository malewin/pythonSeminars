#  Задача No17. Решение в группах
# Дан список чисел. Определите, сколько в нем встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4] Output: 6
 

from random import randint # необходим модуль для функции рандомного заполнения
n = int(input('сколько чисел в вашем списке?: ')) # количество элементов в рандомном списке
minRandBorder = int(input('какое минимальное значение элемента в диапазоне элементов вашего рандомного списка чисел?: ')) # минимум диапазона значений в списке
maxRandBorder = int(input('какое максимальное значение элемента в диапазоне элементов вашего рандомного списка чисел?: ')) # максимум диапазона значений в списке
listOfDiffValue = [] # создаем список для автозаполнения
uniqueValueInList = 0 # количество уникальных значений

def autofill(amount, minBorder, maxBorder): # метод автозаполнения массива элементами: от min до maz
    list_comprehension = [randint(minBorder,maxBorder) for i in range(abs(amount))] # взял по модулю на случай если клиент введёт значение < 0
    return list_comprehension

listOfDiffValue = autofill(n, minRandBorder, maxRandBorder)
print(listOfDiffValue)

listOfUniqueValue = []

# можно просто конвертировать список в множество(что является априори коллекцией с уникальными элементами) и вычислить длинну множества

# convertSet = set(listOfDiffValue) # конвертируем список в множество
# uniqueValueInList = len(convertSet) # узнаем длину множества с уникальными значениями
# print(uniqueValueInList)

# либо алгоритмически
def solution(userList):
    for i in userList:
        if i not in listOfUniqueValue:
            listOfUniqueValue.append(i)
    return listOfUniqueValue

print(len(solution(listOfDiffValue)))



