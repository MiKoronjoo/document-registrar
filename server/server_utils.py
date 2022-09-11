from web3 import Web3
from web3.middleware import geth_poa_middleware

from abi import REGISTRAR_ABI


class Registrar:
    def __init__(self, address: str, rpc_url: str):
        self.w3 = Web3(Web3.HTTPProvider(rpc_url))
        self.w3.middleware_onion.inject(geth_poa_middleware, layer=0)
        self.contract = self.w3.eth.contract(Web3.toChecksumAddress(address), abi=REGISTRAR_ABI)

    def register(self, file_hash: str, title: str, author: str, sign: dict, private_key: str) -> str:
        if not file_hash.startswith('0x'):
            file_hash = '0x' + file_hash
        sender_address = self.w3.eth.account.privateKeyToAccount(private_key).address
        raw_tx = self.contract.functions.register(file_hash,
                                                  title,
                                                  author,
                                                  sign['v'],
                                                  sign['r'],
                                                  sign['s'])
        built_tx = raw_tx.buildTransaction({
            'from': sender_address,
            'nonce': self.w3.eth.get_transaction_count(sender_address)
        })

        signed_tx = self.w3.eth.account.sign_transaction(built_tx, private_key)
        self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        # self.w3.eth.wait_for_transaction_receipt(signed_tx.hash)
        return self.w3.toHex(signed_tx.hash)
