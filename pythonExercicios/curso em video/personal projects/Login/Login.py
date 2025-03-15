from modules.interface import *
from modules.file import *

'''
def login(filename):
    global loggedin
    a = open(filename)
    while True:
        user = str(input("Usuario: "))

        if user not in a:
            print("Usuario desconhecido")

        else:
            password = str(input("Senha: "))

            if dict_users[user] == password:
                logged_in = dict_users.keys().get(user)
                print(f'Ola, {logged_in}')
                break


def register(filename):
    a = open(filename, 'at')
    while True:
        user = str(input("Usuario: "))
        if not user.isalnum():
            print('Usuario Invalido')

        if user in a:
            print("Este usuario ja esta registrado.")

        elif user not in a:
            while True:
                # print("eu não vou checar a força da sua senha, se for facil, a culpa é sua!")
                print('A senha precisa ter:\n'
                      '- minimo de 6 caracteres\n'
                      '- letras e numeros\n'
                      '- letras minusculas e maiusculas\n'
                      '- characteres especiais\n')
                pw = str(input("Senha: "))
                if (len(pw) >= 6
                        and pw.isalpha()
                        and pw.isnumeric()
                        and not pw.islower()
                        and not pw.isupper()
                        and not pw.isalnum()):
                    break
            break
    a.write(f'{user};{pw}')
'''

file = "registeredPeople.txt"

if not file_exists(file):
    create_file(file)

loggedin = False
while True:
    down()
    sleep(1.5)
    if not loggedin:
        print(f'Status: {Color["red"]}not logged in{Color[""]}')
        choice = str(input('[-1] Encerrar\n'
                           '[ 0] Register\n'
                           '[ 1] Login\n'
                           '>')).strip().upper()

        if choice in ['-1', 'ENCERRAR']:
            break
        elif choice in ['1', 'LOGIN']:
            down()
            loggedin = login(file)
        elif choice in ['0', 'REGISTER']:
            down()
            register(file)

    elif loggedin:
        print(f'Status: {Color["green"]}logged in{Color[""]}')
        choice = str(input("[-1] Sair\n"
                           ">")).strip().upper()
        if choice in ['-1', 'SAIR']:
            loggedin = False
