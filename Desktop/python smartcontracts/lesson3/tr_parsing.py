# параметр exit code даёт инфо о статусе транзы либо о причине её обрыва (более подробно какие есть:
# https://docs.ton.org/learn/tvm-instructions/tvm-exit-codes)

import requests
import asyncio
from pathlib import Path
from pytonlib import TonlibClient
from pytonlib.utils.tlb import Transaction, Slice, Cell, deserialize_boc
from tonsdk.utils import b64str_to_bytes
from tonsdk.contract.wallet import Wallets, WalletVersionEnum

async def clientInit():
    url = 'https://ton.org/global-config.json'

    config = requests.get(url).json()

    keystore_dir = '/tmp/ton_keystore'
    Path(keystore_dir).mkdir(parents=True, exist_ok=True)

    client = TonlibClient(ls_index=0, config=config, keystore=keystore_dir, tonlib_timeout=15)

    await client.init()

    return client

async def main():                      # метод определения фазы в транзакции (в стандартных либах нету)
    client = await clientInit()
    trs = await client.get_transactions(account='EQAJhQfbNtmaWpYogVoo59slpxw8YLv3HluxOOPPHHhUnGSw', limit=10)

    for tr in trs:
        cell = deserialize_boc(b64str_to_bytes(tr['data']))
        tr_data = Transaction(Slice(cell))
        com_ph = tr_data.description.compute_ph
        act_ph = tr_data.description.action
        if com_ph.type == 'tr_phase_compute_vm':
            # if com_ph.exit_code == 1 or com_ph.exit_code == 0:
            #     return True
            # else:
            #     return False
            print('compute phase exit code is', com_ph.exit_code)
        if act_ph is not None:
            # if act_ph.exit_code == 1 or act_ph.exit_code == 0:
            #     return True
            # else:
            #     return False
            print('action phase exit code is', act_ph.result_code)
        print(tr)

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
