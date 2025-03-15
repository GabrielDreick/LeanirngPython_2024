# ======================================================================================================================
# Crie um program que tenha uma função leiaint(), que vai funcionar de forma semelhante a função input() do Python,
# so que fazendo a validação para aceitar apenas um valor numerico.
#
# Ex:
# n = leiaint('digite um n')
# ======================================================================================================================
C = {"": "\033[0m",
     "y": "\033[38;2;255;255;0m",
     "r": "\033[38;2;255;0;0m"}


def leiaint(txt=''):
    while True:
        num = input(txt)
        if num.isnumeric():
            num = int(num)
            return num
        else:
            print(f'{C["r"]}Não é um {C["y"]}numero inteiro{C["r"]} valido{C[""]}')


# ╔════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║                                                    MAIN PROGRAM                                                    ║
# ╚════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
n = leiaint('digite um numero: ')
print(f'voce digitou o numero {C["y"]}{n}{C[""]}')

# fim
