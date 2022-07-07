import os
import subprocess
from typing import Iterable

cur_dir = os.path.dirname(os.path.abspath(__file__))


def create_py_from_ui(paths: Iterable):
    for file in paths:
        out_file = file[:-2] + 'py'
        p1 = subprocess.check_call(f'pyuic5 "{os.path.join(cur_dir, file)}" -o "{os.path.join(cur_dir, out_file)}"')


def create_py_from_ui_folder():
    uis = set()
    for file in os.listdir(cur_dir):
        if file[-3:] == '.ui':
            uis.add(file)
    print(uis)
    create_py_from_ui(uis)


def check_and_create_py_from_ui():
    pys = set()
    uis = set()

    for file in os.listdir(cur_dir):
        if file[-3:] == '.ui':
            uis.add(file)
        if file[-3:] == '.py':
            pys.add(file[:-2] + 'ui')

    need_create = uis - pys
    print(need_create)
    create_py_from_ui(need_create)


if __name__ == '__main__':
    check_and_create_py_from_ui()
