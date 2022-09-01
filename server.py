from flask import Flask, jsonify, request

from config import PRIVATE_KEY, CONTRACT_ADDRESS
from utils import Registrar

app = Flask(__name__)
contract = Registrar(CONTRACT_ADDRESS)


class MissRequiredParam(Exception):
    def __init__(self, param_name):
        super(MissRequiredParam, self).__init__(f'Required Param `{param_name}` is missing')


def error_handler(func):
    def wrapped_func(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except Exception as ex:  # TODO: organize exceptions
            print(ex)  # TODO: use traceback instead
            return jsonify(status='Error', message=str(ex)), 400
        else:
            return result

    wrapped_func.__name__ = func.__name__
    return wrapped_func


@app.route('/registerHash', methods=['POST'])
def register_hash():
    params = request.get_json()
    for param in ('hash', 'title', 'author', 'v', 'r', 's'):
        if param not in params:
            raise MissRequiredParam(param)

    tx_hash = contract.register(
        params['hash'],
        params['title'],
        params['author'],
        dict(v=params['v'], r=params['r'], s=params['s']),
        PRIVATE_KEY
    )  # TODO: check the transaction status
    return jsonify(status='success', tx_hash=tx_hash), 200


@app.route('/getOK', methods=['GET'])
def get_ok():
    return 'ok'
