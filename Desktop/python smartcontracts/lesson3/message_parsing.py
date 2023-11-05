# параметр exit code даёт инфо о статусе транзы либо о причине её обрыва (более подробно какие есть:
# https://docs.ton.org/learn/tvm-instructions/tvm-exit-codes)
# op_code - 'operation' in transaction
# исходя из первых 32 бит в массиве байтов сообщения определяется op_code  а далее выбирается class 
# подходящий под определённый op_code и уже в нем понимаем какой метож для парсинга использовать. 
# в данном примере prefix (op_code) = '7362d09c' (in hex2ba formate) - class JettonBurnNotificationMessage

import requests
import asyncio
from pathlib import Path
from pytonlib import TonlibClient
from pytonlib.utils.tlb import Transaction, Slice, Cell, deserialize_boc, CommentMessage, JettonInternalTransferMessage, JettonBurnNotificationMessage
from tonsdk.utils import b64str_to_bytes
from tonsdk.contract.wallet import Wallets, WalletVersionEnum
from tonsdk.contract import Address

async def clientInit():
    url = 'https://ton.org/global-config.json'

    config = requests.get(url).json()

    keystore_dir = '/tmp/ton_keystore'
    Path(keystore_dir).mkdir(parents=True, exist_ok=True)

    client = TonlibClient(ls_index=2, config=config, keystore=keystore_dir, tonlib_timeout=15)

    await client.init()

    return client

async def decodingComment():                          # метод декодирования сообщения-комментария
    message = 'AAAAAHRoYW5rIHlvdSBmb3IgbW9uZXk='
    cell = Cell()
    cell.data.from_bytes(b64str_to_bytes(message))
    print(cell.data.data.to01())   # первые 32 бита - нули (оп код)
    result = CommentMessage.parse(Slice(cell))
    print(result.text_comment)

async def jetonAmountParsing():              # метод определения количества жетонов в транзакции        
    client = await clientInit()
    trs = await client.get_transactions(account='EQBDPuoMs6Zl5fJdp0pe2GCc3SVnVVxRvmgZVf8ymwqWDGJT', limit=1) # получение последней транзакции кошелька жетона

    for tr in trs:
        print(tr)
        cell = deserialize_boc(b64str_to_bytes(tr['out_msgs'][0]['msg_data']['body']))
        result = JettonInternalTransferMessage(Slice(cell))
        print(result.amount)                             

async def jetonAmountAndSenderAddressDetecting():    # метод определения количества жетонов в транзакции и кошелька отправителя
    client = await clientInit()
    trs = await client.get_transactions(account='EQB5DER03H1uhKGX6BJh_IWa_zV9MzvH2lcy6t30tZ9k4RSL', limit=3) # получение последних 3 транзакций кошелька (с тон и жетонами)

    for tr in trs:
        print(tr)
        try:
            cell = deserialize_boc(b64str_to_bytes(tr['out_msgs'][0]['msg_data']['body']))
            result = JettonInternalTransferMessage(Slice(cell))
            print(result.amount)     
        except: pass

        try:
            body = tr['in_msg']['msg_data']['body']
            cell = deserialize_boc(b64str_to_bytes(body))
            result = JettonBurnNotificationMessage(Slice(cell))
            sender_address = Address(str(result.sender.workchain_id) + ':' + str(result.sender.address)).to_string(True, True, True)
            print(result.amount, sender_address)
        except: pass



if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(decodingComment())