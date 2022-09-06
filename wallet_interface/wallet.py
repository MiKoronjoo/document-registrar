import hashlib
import binascii
import os
import pathlib
import random
import re
import sqlite3
import sys

import eth_account
from mnemonic_utils import mnemonic_to_private_key
from utils import decrypt_message, encrypt_message
from config import DB_PATH


def exe_query(query: str, params: tuple = ()):
    con_obj = sqlite3.connect(DB_PATH)
    courser = con_obj.execute(query, params)
    res = courser.fetchall()
    con_obj.commit()
    con_obj.close()
    return res


def create_database_if_not_exists():
    with open('schema.sql') as fp:
        queries = fp.read().split(';')
    for q in queries:
        if q:
            exe_query(q)


class Account:
    def __init__(self, private_key: str, name: str, is_imported: bool):
        self.private_key = private_key
        self.name = name
        self.address = eth_account.Account.from_key(private_key).address
        self.is_imported = is_imported


class Wallet:
    def __init__(self):
        found = exe_query('SELECT * FROM Wallet LIMIT 1')
        if not found:
            self.seed_phrase = ''
            self.count = 0
            self.password_hash = ''
        else:
            self.seed_phrase = found[0][0]
            self.count = found[0][1]
            self.password_hash = found[0][2]
        self.is_lock = True
        self.accounts = []
        self.password = ''
        self.selected_index = 0

    def check_database(self) -> bool:
        return bool(exe_query('SELECT * FROM Wallet LIMIT 1'))

    @property
    def selected(self) -> Account:
        return self.accounts[self.selected_index]

    def set_password(self, password: str):
        assert 8 <= len(password) <= 32, 'Password length must between 8 and 32 chars'
        self.password_hash = hashlib.sha224(password.encode()).hexdigest()
        self.password = password

    def _load_accounts(self, password: str):
        found = exe_query('SELECT * FROM Account')
        self.accounts.clear()
        for acc in found:
            _, name, enc_private_key, imported = acc
            private_key = decrypt_message(enc_private_key, password)
            self.accounts.append(Account(private_key, name, imported))

    def _get_next_private_key(self):
        derivation_path_prefix = "m/44'/60'/0'/0/"
        c = exe_query('SELECT count FROM Wallet')[0][0]
        pk = mnemonic_to_private_key(self.seed_phrase, f"{derivation_path_prefix}{c}")
        return str(binascii.hexlify(pk), 'utf-8')

    def unlock(self, password: str):
        assert hashlib.sha224(password.encode()).hexdigest() == self.password_hash, 'Incorrect password'
        self.seed_phrase = decrypt_message(self.seed_phrase, password)
        self._load_accounts(password)
        self.is_lock = False
        self.password = password

    def lock(self):
        self.seed_phrase = exe_query('SELECT enc_seed_phrase FROM Wallet LIMIT 1')[0][0]
        self.accounts.clear()
        self.is_lock = True
        self.password = ''

    def create_account(self, name: str):
        assert not self.is_lock, 'Wallet is lock'
        private_key = self._get_next_private_key()
        enc_private_key = encrypt_message(private_key, self.password)
        exe_query('INSERT INTO Account (name, enc_private_key, imported) VALUES (?, ?, ?)',
                  (name, enc_private_key, False))
        exe_query('UPDATE Wallet SET count = count + 1')
        self.selected_index = len(self.accounts)
        self.accounts.append(Account(private_key, name, False))

    def import_account(self, private_key: str, name: str):
        assert not self.is_lock, 'Wallet is lock'
        assert re.match(r'^[a-fA-F0-9]{64}$', private_key), 'Invalid private key'

        enc_private_key = encrypt_message(private_key, self.password)
        exe_query('INSERT INTO Account (name, enc_private_key, imported) VALUES (?, ?, ?)',
                  (name, enc_private_key, True))
        self.selected_index = len(self.accounts)
        self.accounts.append(Account(private_key, name, True))

    def create_wallet(self, length: int):
        assert self.password, 'Password not set yet'
        seed_phrase = random_seed_phrase(length)
        enc_seed_phrase = encrypt_message(seed_phrase, self.password)
        exe_query('DELETE FROM Wallet')
        exe_query('INSERT INTO Wallet (enc_seed_phrase, password_hash) VALUES (?, ?)',
                  (enc_seed_phrase, hashlib.sha224(self.password.encode()).hexdigest()))
        self.is_lock = False
        self.create_account('Main Account')
        self.seed_phrase = enc_seed_phrase
        self.unlock(self.password)
        return seed_phrase

    def import_wallet(self, seed_phrase: str):
        assert self.password, 'Password not set yet'
        enc_seed_phrase = encrypt_message(seed_phrase, self.password)
        exe_query('DELETE FROM Wallet')
        exe_query('INSERT INTO Wallet (enc_seed_phrase, password_hash) VALUES (?, ?)',
                  (enc_seed_phrase, hashlib.sha224(self.password.encode()).hexdigest()))
        self.is_lock = False
        self.create_account('Main Account')
        self.seed_phrase = enc_seed_phrase
        self.unlock(self.password)
        return seed_phrase


def generate_seed_phrase(entropy: str) -> str:
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
    return ' '.join(seed)


def random_seed_phrase(length: int) -> str:
    if length not in (12, 15, 18, 21, 24):
        raise ValueError(
            f'seed phrase length should be one of the following: [12, 15, 18, 21, 24], but it is not ({length}).')
    l = length + length // 3
    entropy = ''.join(('0%x' % random.randrange(256))[-2:] for _ in range(l))
    return generate_seed_phrase(entropy)
