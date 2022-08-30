from pprint import pprint

import eth_account
from eth_account.messages import encode_defunct
from web3 import Web3


def sign_message(types: list, params: list, private_key: str):
    signature = Web3.toHex(Web3.soliditySha3(types, params))
    message = encode_defunct(hexstr=signature)
    res = eth_account.account.Account.signHash(message.body, private_key)
    return dict(
        v=res.v,
        r=Web3.toHex(res.r),
        s=Web3.toHex(res.s),
    )


if __name__ == '__main__':
    pprint(sign_message(['bytes32', 'string'],
                        ['0x0000000000000000000000000000000000000000000000000000000000000000', 'title'],
                        'PRIVATE_KEY'))
