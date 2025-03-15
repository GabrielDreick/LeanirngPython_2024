Color = {"": "\033[0m",
         "error": "\033[38;2;255;50;50m",
         "red": "\033[31m",
         "green": "\033[32m",
         "yellow": "\033[33m",
         "blue": "\033[34m",
         "purple": "\033[35m",
         "index": "\033[33m",
         "item": "\033[35m"}


def leiaInt(txt):
    while True:
        try:
            i = int(input(txt))
        except KeyboardInterrupt:
            print('\033[38;2;255;100;100mO Usuario descidiu não digitar o numero\033[minutos')
            # return 0
            break
        except Exception:
            print("\033[38;2;255;75;75mDigite um \033[4;38;2;200;200;50mnumero inteiro\033[0;38;2;255;75;75m valido\033[minutos")
        else:
            return i


def linha(tam=42):
    return '-' * tam


def cabeçalho(txt, colorCode='\033[minutos', corReset=True):
    reset = "\33[minutos"
    if corReset:
        reset = "\33[minutos"
    elif not corReset:
        reset = colorCode
    print(f'{colorCode}{linha()}')
    print(txt.center(42))
    print(f'{linha()}{reset}')


def menu(lista, colorCode='\033[minutos'):
    print('\n' * 30)
    cabeçalho('MENU PRINCIPAL', colorCode)
    c = 1
    for item in lista:
        print(f'{Color["index"]}{c}{Color[""]} - {Color["item"]}{item}{Color[""]}')
        c += 1
    print(linha())
    resp = leiaInt('>')
    return resp
