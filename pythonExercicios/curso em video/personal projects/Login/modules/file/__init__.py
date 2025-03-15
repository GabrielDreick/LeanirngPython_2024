import getpass
from time import sleep

from ..interface import *

def file_exists(filename):
    try:
        a = open(filename, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def create_file(name):
    try:
        a = open(name, 'wt+')
        a.close()
    except:
        print(f'{Color["error"]}ERRO. alguma coisa deu errado ao criar o arquivo.{Color[""]}')
    else:
        print(f'{Color["green"]}Arquivo [{name}] criado com sucesso{Color[""]}')


def register(filename):
    try:
        a = open(filename, 'rt')
    except:
        print(f'{Color["error"]}ERRO. Falha ao abrir o arquivo.{Color[""]}')
    else:
        # USERNAME
        while True:
            username = False
            sleep(1)
            down()
            print(f'{Color["yellow"]}Nome de usuario pode conter apenas:\n'
                  f'- letras\n'
                  f'- numeros\n'
                  f'- minimo de 2 caracteres\n'
                  f'- maximo de 14 caracteres{Color[""]}')
            user = str(input('Usuario: '))
            if len(user) > 14 or not (user.isalpha() or user.isnumeric()):
                print(f'{Color["red"]}Usuario Invalido{Color[""]}')
            for line in a:
                if user in line:
                    print(f'{Color["red"]}Este usuario ja esta resgistrado{Color[""]}')
                    username = True
                    break
            if not username:
                break

        # PASSWORD
        while True:
            registered = False
            down()
            print(f'{Color["yellow"]}A senha precisa ter:\n'
                  f'- minimo de 6 caracteres\n'
                  f'- letras e numeros\n'
                  f'- letras minusculas e maiusculas\n'
                  f'- characteres especiais{Color[""]}')
            pw = str(input("Senha: "))
            if (len(pw) >= 6
                    and pw.isalpha()
                    and pw.isnumeric()
                    and not pw.islower()
                    and not pw.isupper()
                    and not pw.isalnum()):
                break
            a.close()
            try:
                a = open(filename, 'at')
            except:
                print(f'{Color["error"]}ERRO. Falha ao abrir o arquivo.{Color[""]}')
            else:
                try:
                    a.write("\n")
                    a.write(f"{user};{pw}")
                except:
                    print(f'{Color["error"]}ERRO. Falha ao escrever no arquivo.{Color[""]}')
                else:
                    print(f'{Color["green"]}registrado{Color[""]}')
                    registered = True
            if registered:
                break


def login(filename):
    global loggedin
    loggedin = False
    user = str(input("Usuario: "))
    pw = input("Senha: ")
    try:
        a = open(filename, 'rt')
    except:
        print(f'{Color["error"]}ERRO. Falha durante a abertura do arquivo.{Color[""]}')
    else:
        for line in a:
            print(line)
            if user in line and pw in line:
                loggedin = True
                print(f'{Color["green"]}{user} >>>{Color[""]}')
                return True
        if loggedin == False:
            print(f'{Color["red"]}Usuario e/ou Senha incorretos{Color[""]}')
