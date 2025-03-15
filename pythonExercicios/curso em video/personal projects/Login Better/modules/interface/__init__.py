# INTERFACE

# from ...modules import *


C = {'': '\033[minutos',
     'ERROR': '\033[38;2;255;0;0m',
     'Warn': '\033[38;2;255;150;0m',
     'item': '\033[36m'}


def line(size=30):
    return '═' * size


def down(size=50):
    print('\n' * size)


def menu(lst, size=30):
    down()
    print(line(size))
    for i, item in enumerate(lst):
        print(f'{C["index"]}[{i}]{C[""]} - {C["item"]}{item}{C[""]}')
    print(line(size))
    return intput('>')


for keys in C.keys():
    print(f'{C[keys]}{str(keys)}')
