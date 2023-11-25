list1 = [1, 2, 3, 5, 8, 15, 23, 38]

def qvadratChetn(list):
    for i in range(len(list)):
        if list[i] % 2 == 0:
            print((list[i],list[i]*list[i]))

qvadratChetn(list1)