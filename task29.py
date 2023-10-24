# Задача No29. Решение в группах
# Ваня и Петя поспорили, кто быстрее решит следующую задачу: “Задана последовательность неотрицательных целых чисел. 
# Требуется определить значение наибольшего элемента последовательности, которая завершается первым встретившимся нулем (число 0 не входит в последовательность)”. 
  
from random import randint # необходим модуль для функции рандомного заполнения
n = int(input('сколько чисел в вашем списке?: ')) # количество элементов в рандомном списке
minRandBorder = int(input('какое минимальное значение элемента в диапазоне элементов вашего рандомного списка чисел?: ')) # минимум диапазона значений в списке
maxRandBorder = int(input('какое максимальное значение элемента в диапазоне элементов вашего рандомного списка чисел?: ')) # максимум диапазона значений в списке
listOfDiffValue = [] # создаем список для автозаполнения

def autofill(amount, minBorder, maxBorder): # метод автозаполнения массива элементами: от min до max
    list_comprehension = [randint(minBorder,maxBorder) for i in range(abs(amount))] # взял по модулю на случай если клиент введёт значение < 0
    return list_comprehension

listOfDiffValue = autofill(n, minRandBorder, maxRandBorder)
print(f'Ваш изначальный список: {listOfDiffValue}')

def listSeparator(userList):
    maxValue = userList[0]
    for i in userList:
        if i == 0:
            break       
        if maxValue < i:
            maxValue = i
        else:
            continue
    return maxValue

print(f'Максимальный элемент до первого нуля в вашем списке: {listSeparator(listOfDiffValue)}')