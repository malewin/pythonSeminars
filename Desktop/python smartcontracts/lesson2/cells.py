# вычленяем адресс из ячейки в сообщении/

from tonsdk.boc import Cell, begin_cell
from tonsdk.contract import Address # библиотека для сохранения адресса
import bitarray # библиотека чтоб сохранить 28 нулей припереводе в интовое значение hex-вида


address = 'UQCD39VS5jcptHL8vMjEXrzGaRcCVYto7HUn4bpAOg8xqEBI'

message = begin_cell()\
    .store_uint(15, 32)\
    .store_address(Address(address))\
    .store_coins(10000)\
    .end_cell()


if __name__ == '__main__':
    array = message.bits.array # переводим в массив байтов
    # print(message) 
    # print(array)

    x = bitarray.bitarray()
    x.frombytes(array)
    # print(x.to01())

    op_code = int(x[:32].to01(), 2)
    # print(op_code)
    del x[:32] # удаляем ненужные биты информации из массива

    # print(bin(int(array.hex(), 16)))  # без 28 нулей
    del x[:3] # посмотрели в store_address -> write_address методе какие биты что значат и удалили ненужные

    wc = int(x[:8].to01(), 2)
    del x[:8]

    hash_part = hex(int(x[:256].to01(), 2))

    address = str(wc) + ':' + str(hash_part.split('0x')[1]) # сплит убирает 0х из адресса в хекс-форме

    # print(address)
    print(Address(address).to_string(True, True, True)) # to_string(true, true, true) - перерводит в userFriendlyBounceableForm

    del x[:256]

    l = int(x[:4].to01(), 2)

    del x[:4]

    amount = int(x[:l * 8].to01(), 2)
    print(amount)

# далее способ парсинга ячейки с помощью библиотеки поддерживающей "СЛАЙСЫ"
# нужно удалить библиотеку tonsdk и поставить её форк от DAO чтото там..
# from tonsdk.boc import Slice - импортировать метод слайсов и далее код/

# def tonsdk_parsing():
#     slice = Slice(message) # применили метод к нашему сообщению с ячейкой и присвоили в перменную

#     op_code = slice.read_uint(32)
#     address = slice.read_msg_addr().to_string(True, True, True)
#     coins = slice.read_coins()

#     print(op_code, address, coins)



