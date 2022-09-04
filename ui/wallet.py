import hashlib
import binascii
import os
import pathlib
import random

from mnemonic_utils import mnemonic_to_private_key


def generate_seed_phrase(entropy: str):
    data = binascii.unhexlify(entropy.strip())
    if len(data) not in (16, 20, 24, 28, 32):
        raise ValueError(
            f'Data length should be one of the following: [16, 20, 24, 28, 32], but it is not ({len(data)}).')
    h = hashlib.sha256(data).hexdigest()
    b = bin(int(binascii.hexlify(data), 16)
            )[2:].zfill(len(data) * 8) + bin(int(h, 16))[2:].zfill(256)[: len(data) * 8 // 32]
    with open(os.path.join(str(pathlib.Path(__file__).parent), 'english_words.txt')) as fp:
        wordlist = [w.strip() for w in fp.readlines()]
    seed = []
    for i in range(len(b) // 11):
        index = int(b[11 * i:11 * (i + 1)], 2)
        seed.append(wordlist[index])
    return seed


def random_seed_phrase(length: int):
    if length not in (12, 15, 18, 21, 24):
        raise ValueError(
            f'seed phrase length should be one of the following: [12, 15, 18, 21, 24], but it is not ({length}).')
    l = length + length // 3
    entropy = ''.join(('0%x' % random.randrange(256))[-2:] for _ in range(l))
    return generate_seed_phrase(entropy)


if __name__ == '__main__':
    sp = random_seed_phrase(24)
    print(' '.join(sp))
    DERIVATION_PATH_PREFIX = "m/44'/60'/0'/0/"
    pk = mnemonic_to_private_key(' '.join(sp), f"{DERIVATION_PATH_PREFIX}0")
    print(str(binascii.hexlify(pk), 'utf-8'))
