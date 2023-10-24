# Задача No25. Решение в группах
# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался. 
# Количество повторов добавляется к символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию .split()


userString = list(input("Введите текст/ строку: ").replace(" ", ''))
print(userString)

def reAdder(text):
    counter = 1   # конкретный счетчик количества элемента приписываемый в возвращаемое значние конкретного елемента
    for i in range(len(text)):
        for j in set(text):
            if i+1 != len(text):                # устраняем ошибку выхода индексов за границы массива
                if text[i] == text[i+1]:
                    text.pop(i+1)
                    text.insert((i+1),f"{text[i]}_{counter}")
                    counter += 1
            counter = 1
    return text

print(reAdder(userString))



