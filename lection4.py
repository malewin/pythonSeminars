# list1 = [1, 2, 3, 5, 8, 15, 23, 38]
# res = map(int, list1) # функция map принимает два аргумента: функцию которую применит к каждому итерируемому обьекту во втором аргументе
# res = filter(lambda x: x % 2 == 0, res) # функция filter выдает только те значения которые true после двоеточия из опять же иттерируемого аргумента 2
# res = list(map(lambda x: (x, x**2), res))
# print(res)

#zip-функция берет несколько иттерируемых наборов (коллекции) и создает новый набор из кортежей значений взятых соответственно из каждой коллекции
# создает по минимальнмоу количеству во входящем наборе, пример:
# clients = ['tondomainer', 'author', 'elector', 'fuhao']
# domainsValue = [1140, 381, 150, 20]
# paidTonAmount = ['10500ton', '9700ton', '15000ton', '20000ton']
# slovar = list(zip(clients, domainsValue, paidTonAmount))
# print(slovar)

#функция enumerate() принимает на вход список и выдает список из кортежей где 1ое-индекс значения, 2ое - само значение списка
# clients = ['tondomainer', 'author', 'elector', 'fuhao']
# print(dict(enumerate(clients)))
# print(tuple(enumerate(clients)))
# print(set(enumerate(clients)))
# print(list(enumerate(clients)))
