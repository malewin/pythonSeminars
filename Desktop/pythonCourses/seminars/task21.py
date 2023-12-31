# Задача No21. Решение в группах
# Напишите программу для печати всех уникальных значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# Примечание: Список словарей задан изначально. Пользователь его не вводит. 

lst = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]
lst1 = set()

# for i in lst:      # конструкция №1
#     for j in i:     # j - ключ, i - словарь
#         lst1.add(i[j])    # добавляем элемент нового множества со значением словаря по ключу

# for i in lst:        # конструкция №2
#     for j in i.values():  # j - значение (так как iterable уже не сам словарь, а значение из элементов(словарей) списка)
#         lst1.add(j)       # стало быть доавбляем уже само значение

for i in lst:        # конструкция №3
    for j, y in i.items():  # j - связка "ключ+значение" (так как iterable )
        lst1.add(y)       # стало быть доавбляем уже само значение

print(lst1)
