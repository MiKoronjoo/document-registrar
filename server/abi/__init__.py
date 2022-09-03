import json
import os
import pathlib


def get_path(file_name):
    return os.path.join(str(pathlib.Path(__file__).parent), file_name)


with open(get_path('registrar_abi.json'), 'r') as fp:
    REGISTRAR_ABI = json.load(fp)
