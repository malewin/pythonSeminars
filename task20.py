"""
Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. В случае с английским алфавитом очки распределяются так:
● A, E, I, O, U, L, N, S, T, R – 1 очко;
● D, G – 2 очка;
● B, C, M, P – 3 очка;
● F, H, V, W, Y – 4 очка;
● K – 5 очков;
● J, X – 8 очков;
● Q, Z – 10 очков.
А русские буквы оцениваются так:
● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
● Д, К, Л, М, П, У – 2 очка;
● Б, Г, Ё, Ь, Я – 3 очка;
● Й, Ы – 4 очка;
● Ж, З, Х, Ц, Ч – 5 очков;
● Ш, Э, Ю – 8 очков;
● Ф, Щ, Ъ – 10 очков.
Напишите программу, которая вычисляет стоимость введенного пользователем слова. Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.
                    Ввод:
ноутбук
Вывод:
12
"""

slovo = input('enter your word / введите ваше слово: ').lower()
engAlphabet = {'a':1, 'e':1, 'i':1, 'o':1, 'u':1, 'l':1, 'n':1, 's':1, 't':1, 'r' :1, 'd':2, 'g':2, 'b':3, 'c':3, 'm':3, 'p':3, 'f':4, 'h':4, 'v':4, 'w':4, 'y':4, 'k':5, 'j':8, 'x':8, 'q':10, 'z':10}
rusAlphabet = {'й':4, 'ц':5, 'у':2, 'к':2, 'е':1, 'н':1, 'г':3, 'ш':8, 'щ':10, 'з':5, 'х':5, 'ъ':10, 'ф':10, 'ы':4, 'в':1, 'а':1, 'п':2, 'р':1, 'о':1, 'л':2, 'д':2, 'ж':5, 'э':8, 'ё':3, 'я':3, 'ч':5, 'с':1, 'м':2, 'и':1, 'т':1, 'ь':3, 'б':3, 'ю':8}
# listOfDictionares = [engAlphabet, rusAlphabet]

def languageDetected(dict1, dict2, word): # метод распознавания языка для декомпозиции
    dictionary = {}
    if bool(set(word).intersection(set(dict1))) == True:
        dictionary = dict1
    else:
        dictionary = dict2
    return dictionary

def scoresCounter(dict, word): # метод подсчёта очков
    counter = 0
    for i in word:
        for j,k in dict.items():
            if i==j:
                counter += k
    return counter

result = scoresCounter(languageDetected(engAlphabet, rusAlphabet, slovo), slovo)
print(result)

# print(list('йцукенгшщзхъфывапролджэёячсмитьбю'))

# print(bool(set(engAlphabet).intersection(set(slovo))))

