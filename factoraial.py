n = int(input('от какого числа берём факториал?: ')) # количество элементов в рандомном списке

def factorial(n):
    if n == 1:
        return n
    return n * factorial(n-1)

print(factorial(n))