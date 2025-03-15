from datetime import datetime
import pandas
print()

dt = datetime
dtt = dt.today()


class Time:
    def __init__(self):
        self.day = dtt.day
        self.month = dtt.month
        self.year = dtt.year

        self.time = f"{dtt.hour:0>2}:{dtt.minute:0>2}:{dtt.second:0>2}"

########################################################################################################################


def file_exists(filename):
    try:
        f = open(filename, "r")
        f.close()
    except:
        return False
    else:
        return True


def create_file(filename):
    try:
        f = open(filename, "wt+")
        f.close()
    except Exception as error:
        print(f"create_file: {error}")
    else:
        pass


def open_file(filename, mode='read', act='historico'):
    try:
        f = open(filename, mode[:1])
    except Exception as error:
        print(f"open_file: {error}")
    else:
        try:
            match act:
                case
                case _:
                    err1()
    finally:
        f.close()


def err1():
    print("\033[31m" + "opção invalida" + "\033[m")


def intput(txt=">"):
    while True:
        try:
            n = int(input(txt))
        except ValueError:
            print("Digite um numero inteiro")
        else:
            return n


def menu(lst):
    while True:
        list_index = []
        for c in range(len(lst)-1, -1, -1):
            print(f"[{c}] - {lst[c]}")
            list_index.append(c)
        n = intput()
        if n not in list_index:
            err1()
        elif n in list_index:
            return n


now = Time()
"""print(f'''
===============
day: {now.day}
month: {now.month}
year: {now.year}
time: {now.time}
===============

arquivos:
    compras:
        'compras-{now.year};{now.month};{now.day};{now.time}'
        'compras-{now.year};{now.month-2};{now.day-5};{now.time}'
        'compras-{now.year};{now.month-4};{now.day+4};{now.time}'
''')"""

menu(["Registrar", "Historico"])
