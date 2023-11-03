import requests
import asyncio
from pathlib import Path
from pytonlib import TonlibClient
from wallet_creation import wallet, wallet_address
from tonsdk.utils import to_nano

async def get_seqno(client: TonlibClient, address: str):
    return await client.raw_run_method(method='seqno', stack_data=[], address = wallet_address)

async def main():

    url = 'https://ton.org/testnet-global.config.json'

    config = requests.get(url).json()

    keystore_dir = '/tmp/ton_keystore'
    Path(keystore_dir).mkdir(parents=True, exist_ok=True)

    client = TonlibClient(ls_index=4, config=config, keystore=keystore_dir, tonlib_timeout=15)
    print(wallet.address.to_string(True, True, True, True))

    await client.init()

    query = wallet.create_init_external_message()

    deploy_message = query['message'].to_boc(False)

    print(await get_seqno(client, wallet_address))

    wallet.create_transfer_message(to_addr = 'UQCD39VS5jcptHL8vMjEXrzGaRcCVYto7HUn4bpAOg8xqEBI', amount = to_nano(0.01, 'ton'), seqno = 1)
    
    await client.raw_send_message(deploy_message)

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())