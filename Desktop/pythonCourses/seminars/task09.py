#  Задача No9. Решение в группах
# По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * ... * N 
# (произведение всех чисел от 1 до N) 0! = 1 Решить задачу используя цикл while
# Input: 5
# Output: 120

num = int(input('Введите целое не отрицательное число: '))
result = 1

if(num == 0):
    print(1)

else:
    while (num > 0):
        result *= num
        num -=  1
        print(num)
print(result)



