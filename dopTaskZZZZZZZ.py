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

def CreateCheckingBase(amountOfRefrezherators):
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

print(CreateCheckingBase(n))

def sickDetecting(technicBase):
    j = "anton"
    for i in range(len(technicBase)):
        x = 0  # индекс строки j
        for k in technicBase[i]:
            if k == j[x] and set(j).intersection(set(technicBase[i])):
                x += 1
                continue
            else: