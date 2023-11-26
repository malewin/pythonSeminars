# с помощью лямбда функций определить является ли число 2-х значным
numbers = '8 11 0 -23 140 1'
# print(*filter(lambda x: 10 <= abs(int(x)) <= 99, numbers.split()))
print(*filter(lambda x: len(str(abs(int(x))))==2,numbers.split()))


# x = int(input('Введите двузначное число'))
# if lambda x: 10 <= x <= 99 == False:
#     print(f"число {x} - двузначное")
# else:
#     print(f"число {x} - не двузначное")
