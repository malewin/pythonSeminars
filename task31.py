# найти значение числа из ряда фибоначи

n = int(input('какое по счету число показываем из ряда Фибо?: ')) # количество элементов в рандомном списке

def fib(index):
    if index <= 1:
        return 1
    return fib(index-1) + fib(index-2)
print(fib(n))