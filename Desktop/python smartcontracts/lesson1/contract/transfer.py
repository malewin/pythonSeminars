import asyncio
from wallet_creation import wallet
from pytonlib_toncenter import get_seqno
from pathlib import Path
from pytonlib import TonlibClient
import requests
from make_message import make_message_body
from tonsdk import to_nano

async def main():
    url = 'https://ton.org/testnet-global.config.json'

    config = requests.get(url).json()

    keystore_dir = '/tmp/ton_keystore'
    Path(keystore_dir).mkdir(parents=True, exist_ok=True)

    client = TonlibClient(ls_index=14, config=config, keystore=keystore_dir, tonlib_timeout=15)

    await client.init()

    seqno = await get_seqno(client, address='kQBukJz_h4GmaYHHnPj0dXFLw2hho2sWevHWWrnihqXA0zew') # address of wallet from which will sended the transaction

    query = wallet.create_transfer_message(to_addr='uslovnyy address samogo smartcontracta', amount=to_nano(0.01, 'ton'), # address of smartcontract
                                    seqno=seqno, payload=make_message_body())
    
    message = query['message'].to_boc(False)

    await client.raw_send_message(message)

    if __name__ == '__main__':
        asyncio.get_event_loop().run_until_complete(main())