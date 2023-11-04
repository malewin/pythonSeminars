import requests
import asyncio
from pathlib import Path
from pytonlib import TonlibClient
from tonsdk.utils import to_nano
from tonsdk.contract.wallet import Wallets, WalletVersionEnum

async def clientInit():
    url = 'https://ton.org/testnet-global.config.json'

    config = requests.get(url).json()

    keystore_dir = '/tmp/ton_keystore'
    Path(keystore_dir).mkdir(parents=True, exist_ok=True)

    client = TonlibClient(ls_index=0, config=config, keystore=keystore_dir, tonlib_timeout=15)

    await client.init()

    return client

async def get_seqno(client: TonlibClient, address: str):
    data = await client.raw_run_method(method='seqno', stack_data=[], address = address)
    return int(data['stack'][0][1], 16)

async def main():
    mnemonics = ['suspect', 'indicate', 'absorb', 'educate', 
            'share', 'fossil', 'foam', 'good', 'glare', 
            'predict', 'stem', 'depart', 'domain', 'east', 
            'benefit', 'fragile', 'jelly', 'loyal', 'toilet', 
            'merry', 'pride', 'increase', 'marble', 'erode']
    mnemonics, pub_k, priv_k, wallet = Wallets.from_mnemonics(mnemonics = mnemonics, version = WalletVersionEnum.v3r2, workchain = 0) 

    wallet_address = (wallet.address.to_string(True, True, True, True))

    mnemonics, pub_k, priv_k, new_wallet = Wallets.create(version=WalletVersionEnum.v3r2, workchain=0)

    state_init = new_wallet.create_state_init()['state_init']

    client = await clientInit()

    seqno = await get_seqno(client, wallet_address)

    query = wallet.create_transfer_message(to_addr=new_wallet.address.to_string(), 
                                   amount=to_nano(0.05, 'ton'), seqno=seqno, state_init=state_init)
    
    await client.raw_send_message(query['message'].to_boc())


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())