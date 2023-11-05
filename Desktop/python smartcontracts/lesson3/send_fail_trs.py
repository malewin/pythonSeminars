# генерируем/моделируем сообщение с ошибкой. посмотреть не прошедшие на кошелек транзакции можно на explorer.toncoin.org (@toncx_bot)
# есть две (из нескольких) фазы от которых зависит успешна ли транзакция: compute phase (подготовительная) и action phase (исполняемая)
# у них есть параметр exit code, если exit code =0 или =1 - транзакция считается успешной. (более подробно про фазы https://docs.ton.org/learn/tvm-instructions/tvm-overview)

import asyncio
from TonTools import Wallet, TonApiClient
from secret import mnemonics

async def main():

    client = TonApiClient()
    wallet = Wallet(mnemonics=mnemonics, provider=client)
    # print(await wallet.get_seqno())
    # await wallet.transfer_ton(destination_address='UQCD39VS5jcptHL8vMjEXrzGaRcCVYto7HUn4bpAOg8xqEBI', amount=100, send_mode=0) # sendmode = 2 - игнорирует ошибки в action phase 

    print('\n'.join(list(map(str, (await wallet.get_transactions(10))))))

if __name__ == "__main__":

    # asyncio.get_event_loop().run_until_complete(main())
    asyncio.run(main())

