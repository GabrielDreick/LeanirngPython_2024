# ======================================================================================================================
# Faça um programa que tenha uma função chamada area(),
# que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a area do terreno
# ======================================================================================================================
from time import sleep


def area(a, b):
    are = a * b
    for c in f'A area DE um terreNO COM {a:.2f} Metros de LARgura e {b:.2f} METROS de compriMENTO é {are:.2f} MetrOS':
        print(c, end='')
        sleep(.05)


# PROGRAMA PRINCIPAL =0=0=0=0=0=0=0=0=0=0=0=0=0=0=0=0=0=0=0=0=0=0=0=0=0=0=0=0=0=0=0=0=0=0=0=0=0=0=0=0=0=0=0=0=0=0=0=0=0=
msg = 'POSSO calcular A arEa de um TErreno, so preciso QUE você me DIGA, em metros, '
for letra in msg:
    print(letra, end='')
    sleep(.05)
print()
area(float(input('o comPRImento: ')), float(input('e A largura: ')))

# fim
