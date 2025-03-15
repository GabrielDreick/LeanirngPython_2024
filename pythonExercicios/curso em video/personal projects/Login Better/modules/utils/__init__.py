# UTILS

from ...modules import *
from time import sleep


def intput(txt=''):
    while True:
        try:
            n = int(input(txt))
        except ValueError:
            print('Type and integer')
        else:
            return n
