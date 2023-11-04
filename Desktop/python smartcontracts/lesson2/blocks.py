import requests
import asyncio
from pathlib import Path
from pytonlib import TonlibClient


async def get_client(index):               
    url = 'https://ton.org/global-config.json'

    config = requests.get(url).json()

    keystore_dir = '/tmp/ton_keystore'
    Path(keystore_dir).mkdir(parents=True, exist_ok=True)
  
    client = TonlibClient(ls_index=index, config=config, keystore=keystore_dir, tonlib_timeout=15)

    await client.init()

    return client

async def get_block_transaction(client: TonlibClient, wc, shard, seqno):
    return await client.get_block_transactions(workchain=wc, shard=shard, seqno=seqno, count=40)['transactions']  # count - количество запрашиваемых транзакций (по стоку идет 40)


async def main():
    client = await get_client(0)

    last_master_block = (await client.get_masterchain_info())['last']

    print(await get_block_transaction(client, -1, last_master_block['shard'], last_master_block['seqno']))

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
