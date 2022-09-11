import sys
import traceback

from flask import Flask, jsonify, request

from config import PRIVATE_KEY, CONTRACT_ADDRESS, RPC_URL
from server_utils import Registrar

app = Flask(__name__)
contract = Registrar(CONTRACT_ADDRESS, RPC_URL)


class MissRequiredParam(Exception):
    def __init__(self, param_name):
        super(MissRequiredParam, self).__init__(f'Required Param `{param_name}` is missing')


def error_handler(func):
    def wrapped_func(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except Exception as ex:
            traceback.print_exc(file=sys.stdout)
            print('ERROR:', ex)
            return jsonify(status='Error', message=str(ex)), 400
        else:
            return result

    wrapped_func.__name__ = func.__name__
    return wrapped_func


@app.route('/registerHash', methods=['POST'])
@error_handler
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
    )
    return jsonify(status='success', tx_hash=tx_hash), 200


@app.route('/getOK', methods=['GET'])
def get_ok():
    return 'ok'


if __name__ == '__main__':
    app.run(port=9222)
