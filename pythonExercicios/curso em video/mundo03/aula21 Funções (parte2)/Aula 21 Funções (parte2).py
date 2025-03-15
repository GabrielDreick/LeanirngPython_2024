# help(input)
# print(input.__doc__)

def contador(i, f, p):
    """Faz uma contagem e mostra na tela.
    :param i: Inicio da contagem
    :param f: Fim da contagem
    :param p: Passo da contagem
    :return: Sem retorno
    """
    c = i
    while c <= f:
        print(f'{c}', end=' ')
        c += p
    print('fim')
    # for c in range(i, f, p):


contador(2, 10, 2)

help(contador)


# ##### PARAMETROS OPCIONAIS ##### #
def somar(a=0, b=0, c=0):
    s = a + b + c
    print(f'a soma vale {s}')


somar(3, 2, 5)
somar(8, 4)
somar()


def teste():
    x = 8  # var local
    print(f'na função teste, n vale {n}\n'
          f'na função teste, x vale {x}')


n = 2  # var global
print(f'no programa principal, n vale {n}')
teste()


def funcao():
    global n1
    n1 = 5
    print(f'n1 dentro vale {n1}')


n1 = 2
print(f'n1 fora vale {n1}')
funcao()
print(f'n1 fora vale {n1}')


def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = somar(1, 5, 9)
r2 = somar(1, 7)
r3 = somar(2, 9)
print(f'resultados {r1}, {r2}, {r3}')
print(f'resultado {somar(9, 9, 9)}')


def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'os resultados são {f1}, {f2}, {f3}')


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input("digite um numero: "))
if par(num):
    print('é par')
else:
    print('não é par')
