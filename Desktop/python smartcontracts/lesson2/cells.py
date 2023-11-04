from tonsdk.boc import Cell, begin_cell
from tonsdk.contract import Address

address = 'UQCD39VS5jcptHL8vMjEXrzGaRcCVYto7HUn4bpAOg8xqEBI'

message = begin_cell()\
    .store_uint(15, 32)\
    .store_address(Address(address))\
    .store_coins(10000)\
    .end_cell()



if __name__ == '__main__':

    print(message)