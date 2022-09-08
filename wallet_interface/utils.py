import base64
import hashlib
from typing import Tuple

import eth_account
from cryptography.fernet import Fernet
from eth_account.messages import encode_defunct
from web3 import Web3
from web3.middleware import geth_poa_middleware

from abi import REGISTRAR_ABI


class Registrar:
    def __init__(self, address: str, rpc_url: str):
        self.w3 = Web3(Web3.HTTPProvider(rpc_url))
        self.w3.middleware_onion.inject(geth_poa_middleware, layer=0)
        self.contract = self.w3.eth.contract(Web3.toChecksumAddress(address), abi=REGISTRAR_ABI)

    def send_ether(self, to: str, value: int, private_key: str) -> str:
        sender_address = self.w3.eth.account.privateKeyToAccount(private_key).address
        signed_tx = self.w3.eth.account.signTransaction({
            'from': sender_address,
            'nonce': self.w3.eth.get_transaction_count(sender_address),
            'to': to,
            'value': value,
            'data': b'',
            'gas': 100000,
            'gasPrice': self.w3.eth.gasPrice,
            'chainId': 4
        },
            private_key
        )
        self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        # self.w3.eth.wait_for_transaction_receipt(signed_tx.hash)
        return self.w3.toHex(signed_tx.hash)

    def get_balance(self, address: str) -> float:
        return round(self.w3.eth.get_balance(address) / 1e18, 8)

    def file_timestamp(self, file_hash: str) -> int:
        return self.contract.functions.getTimestamp(file_hash).call()

    def get_info(self, file_hash: str) -> Tuple[str, str, int]:
        return self.contract.functions.documents(file_hash).call()

    def register(self, file_hash: str, title: str, author: str, sign: dict, private_key: str) -> str:
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
        self.w3.eth.wait_for_transaction_receipt(signed_tx.hash)
        return self.w3.toHex(signed_tx.hash)

    def register_without_sign(self, file_hash: str, title: str, private_key: str, gas_price: str = None) -> str:
        sender_address = self.w3.eth.account.privateKeyToAccount(private_key).address
        raw_tx = self.contract.functions.registerWithoutSign(file_hash, title)
        data = {
            'from': sender_address,
            'nonce': self.w3.eth.get_transaction_count(sender_address)
        }
        if gas_price is not None:
            data['gasPrice'] = self.w3.toWei(gas_price, 'gwei')
        built_tx = raw_tx.buildTransaction(data)
        signed_tx = self.w3.eth.account.sign_transaction(built_tx, private_key)
        self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        # self.w3.eth.wait_for_transaction_receipt(signed_tx.hash)
        return self.w3.toHex(signed_tx.hash)

    def update_title(self, file_hash: str, new_title: str, private_key: str) -> str:
        sender_address = self.w3.eth.account.privateKeyToAccount(private_key).address
        raw_tx = self.contract.functions.updateTitle(file_hash, new_title)
        built_tx = raw_tx.buildTransaction({
            'from': sender_address,
            'nonce': self.w3.eth.get_transaction_count(sender_address)
        })

        signed_tx = self.w3.eth.account.sign_transaction(built_tx, private_key)
        self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        # self.w3.eth.wait_for_transaction_receipt(signed_tx.hash)
        return self.w3.toHex(signed_tx.hash)


def hash_file(path: str) -> str:
    with open(path, 'rb') as file:
        bin_file = file.read()
    file_hash = hashlib.sha256(bytearray(bin_file)).hexdigest()
    return file_hash


def sign_with_private_key(file_hash: str, title: str, private_key: str) -> dict:
    return sign_message(['bytes32', 'string'],
                        ['0x' + file_hash, title],
                        private_key)


def sign_message(types: list, params: list, private_key: str) -> dict:
    signature = Web3.toHex(Web3.soliditySha3(types, params))
    message = encode_defunct(hexstr=signature)
    res = eth_account.account.Account.signHash(message.body, private_key)
    return dict(
        v=res.v,
        r=Web3.toHex(res.r),
        s=Web3.toHex(res.s),
    )


def encrypt_message(message, password):
    key = base64.urlsafe_b64encode(password.ljust(32, ' ').encode())
    encoded_message = message.encode()
    f = Fernet(key)
    encrypted_message = f.encrypt(encoded_message)
    return encrypted_message.decode()


def decrypt_message(encrypted_message, password):
    key = base64.urlsafe_b64encode(password.ljust(32, ' ').encode())
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message.encode())
    return decrypted_message.decode()
