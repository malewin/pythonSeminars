"""
доп задача, НЕ дз.
Искусственный интеллект Антон, созданный Гилфойлом, взломал сеть умных холодильников. Теперь он использует их в качестве серверов "Пегого дудочника". 
Помогите владельцу фирмы отыскать все зараженные холодильники.
Для каждого холодильника существует строка с данными, состоящая из строчных букв и цифр, и если в ней присутствует слово "anton" 
(необязательно рядом стоящие буквы, главное наличие последовательности букв), то холодильник заражен и нужно вывести номер холодильника, нумерация начинается с единицы
Формат входных данных
В первой строке подаётся число 
n
n – количество холодильников. В последующих n строках вводятся строки, содержащие латинские строчные буквы и цифры, в каждой строке от 5 до 100 символов.
Sample Input 1:
6
222anton456
a1n1t1o1n1
0000a0000n00t00000o000000n
gylfole
richard
ant0n
Sample Output 1:
1 2 3
Sample Input 2:
9
osfjwoiergwoignaewpjofwoeijfnwfonewfoignewtowenffnoeiwowjfninoiwfen
anton
aoooooooooontooooo
elelelelelelelelelel
ntoneeee
tonee
253235235a5323352n25235352t253523523235oo235523523523n
antoooooooooooooooooooooooooooooooooooooooooooooooooooon
unton
Sample Output 2:
1 2 7 8
"""

n = int(input("Введите сколько холодильников нужно проверить от вируса Гилфойла: "))
refrezherator = ""
virus = 'anton'

def CreateCheckingBase(amountOfRefrezherators):    # метод формирования списка-базы холодильников требующих проверки
    i = 0
    baseList = []
    while i < amountOfRefrezherators:
        refrezherator = input("Введите серийный номер холодильника от 5 до 100 символов: ")
        if len(refrezherator) >= 5 and len(refrezherator) < 100:
            baseList.append(refrezherator)
            i += 1
        else:
            refrezherator = input("Символов больше 100 или меньше 5. Введите серийный номер холодильника ещё раз: ")
    return baseList

base = CreateCheckingBase(n) # задаём "постоянную" переменную чтобы работать с заполненым списком т/к/ через методы будут новые автозаполнения.
print(base)

def itterateList(str1, str2):   # метод рекурсивного среза строки 
    flag = False                
    i = 0                    # индекс строки
    while i < len(str2):
        for k in range(len(str1)):           # для каждого символа в поисковой строке
            if str1[k] == str2[i]:           # если этот символ равен 1ому символу парсируемой строки
                str1 = str1[(k+1):]          # присваиваем входной поисковой строке новый обрезанный от найденного элемента диапазон(срез)
                i += 1                       # повышаем индекс парсируемой строки для поиска следующего элемента и обрезания      
                break                        # без него будет индексрэйнджаут и ничего не будет работать
            elif str1[k] == str2[(len(str2))-1]:  # если иттерации доходят до конечного символа
                flag = True                       # возвращается флаг что операция парсинга одной строки в другой - возможна
            else:
                continue
    return flag     

def sickDetecting(technicBase, sick):
    for i in range(len(technicBase)):
        if itterateList(technicBase[i], sick) == True:
            print(i+1)

print(sickDetecting(base, virus))






# def sickDetecting(technicBase): # метод поиска строки-вируса в каждом элементе списка(серийном номере холодильника)
#     virus = list("anton")       # тот список/строка со значением индексов которого будем сравнивать значения символов строки серийного номера холодильника
#     antiDot = []                
#     for i in range(len(technicBase)):
#         x = 0  # индекс строки virus
#         for k in technicBase[i]:
#             if k == virus[x] and set(virus).intersection(set(technicBase[i])):
#                 antiDot.append(k)
#                 x += 1
#                 continue
#             else:
#                 x += 1
#                 continue
#         if str(antiDot) == str(virus):
#             print(i)
#         else:
#             print("исправляй")
#         antiDot = 0
    
# sickDetecting(base)
        