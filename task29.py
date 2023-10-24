# Задача No29. Решение в группах
# Ваня и Петя поспорили, кто быстрее решит следующую задачу: “Задана последовательность неотрицательных целых чисел. Требуется определить значение наибольшего элемента последовательности, которая завершается первым встретившимся нулем (число 0 не входит в последовательность)”. Однако 2 друга оказались не такими смышлеными. Никто из ребят не смог до конца сделать это задание. Они решили так: у кого будет меньше ошибок в коде, тот и выиграл спор. За помощью товарищи обратились к Вам, студентам.
# Примечание: Программные коды на следующих слайдах
# 30 минут
# Ваня:
# n = int(input())
#  max_number = 1000
#  while n != 0:
#  n = int(input())
#  if max_number > n:
#  max_number = n
#  print(max_number)        
# Петя:
#  n = int(input())
#  max_number = -1
#  while n < 0:
#  n = int(input())
#  if max_number < n:
#  n = max_number
# 30 минут
#  print(n)
  
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
        while i != 0:
            if maxValue < i:
                maxValue = i
    return maxValue

print(listSeparator(listOfDiffValue))