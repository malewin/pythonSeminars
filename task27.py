"""
Задача No27. Решение в группах
Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд, слова разделены одним или большим числом пробелов. Определите, сколько различных слов содержится в этом тексте.
Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells
Output: 13
15 минут
"""

text = input("Enter text: ").replace("."," ").split()
print(text)
print(len(set(text)))


# def wordCounter(resultList):
#     counter = 0
#     for i in range(len(resultList)):
#         for j in resultList:
#             if resultList[i] == j:
#                 counter += 1
#     return counter

# print(wordCounter(text))