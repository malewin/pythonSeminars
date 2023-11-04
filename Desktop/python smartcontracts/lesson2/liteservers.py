# Archive node - архивные ноды хранят блоки от начала до сегодняшнего дня
# Full node - полные ноды хранят инфу о блоках за диапазон времени примерн ов пару недель
# учимся определять тип Ноды

import requests
import asyncio
from pathlib import Path
from pytonlib import TonlibClient
import random


async def archive_ls_detecting():               # метод опеределения архивная ли нода (рандинт секно блока от 2(начало) до 2^12 (то есть 4096))
    url = 'https://ton.org/global-config.json'

    config = requests.get(url).json()

    keystore_dir = '/tmp/ton_keystore'
    Path(keystore_dir).mkdir(parents=True, exist_ok=True)

    for index in range(len(config['liteservers'])):
        
        client = TonlibClient(ls_index=index, config=config, keystore=keystore_dir, tonlib_timeout=15)

        await client.init()

        try:
            print(await client.lookup_block(-1, -9223372036854775808, random.randint(2, 4096)))
            print(index)
        except:
            pass

async def transactions():
    url = 'https://ton.org/global-config.json'

    config = requests.get(url).json()

    keystore_dir = '/tmp/ton_keystore'
    Path(keystore_dir).mkdir(parents=True, exist_ok=True)
        
    client = TonlibClient(ls_index=index, config=config, keystore=keystore_dir, tonlib_timeout=15)

    await client.init()

    await client.get_transactions(account='EQAMoPBaaE_ud88pid9_AW7hjWVz6hWf0XwmJtAdSXq4putF', limit=2) # limit это количетсов транзакций в списке транзакций пр: 1-последняя, 2 - предпоследняя, 
                                                                                                        # если выдаёт ошибку "lt not in db" - значит об этой транзакции лайтсервер уже не помнит


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(archive_ls_detecting())
