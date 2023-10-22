# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), 
# не превосходящие числа N.

n = int(input('До какого числа?: '))
k = 0
list_stepeney = []

while 2**k < n:
    list_stepeney.append(2**k)
    k += 1
print(list_stepeney)