from tonsdk.contract.wallet import Wallets, WalletVersionEnum

mnemonics = ['suspect', 'indicate', 'absorb', 'educate', 
            'share', 'fossil', 'foam', 'good', 'glare', 
            'predict', 'stem', 'depart', 'domain', 'east', 
            'benefit', 'fragile', 'jelly', 'loyal', 'toilet', 
            'merry', 'pride', 'increase', 'marble', 'erode']
mnemonics, pub_k, priv_k, wallet = Wallets.from_mnemonics(mnemonics = mnemonics, version = WalletVersionEnum.v3r2, workchain = 0) # wallets.create()- чтоб создать

if __name__ == '__main__':
    print(mnemonics)
    # print(wallet.address.to_string()) # hex - format (16ричное число)
    # print(wallet.address.to_string(True, True, True)) # привычная форма кошелька
    print(wallet.address.to_string(True, True, True, True)) # test.net - формат