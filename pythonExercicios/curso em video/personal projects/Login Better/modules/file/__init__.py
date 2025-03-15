# FILE

from ...modules import *


def file_exits(filename):
    try:
        f = open(filename, 'rt')
        f.close()
    except:
        return False
    else:
        return True


def create_file(filename):
    try:
        f = open(filename, 'rt+')
        f.close()
    except Exception as err:
        print(err)
    else:
        print("Arquivo criado")
        sleep(1)
