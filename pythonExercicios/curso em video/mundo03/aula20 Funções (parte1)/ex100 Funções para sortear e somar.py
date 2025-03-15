# ======================================================================================================================
# Faça um programa que tenha uma lista chamada numeros e duas funções chamadas sorteia() e somaPar().
# a primeira função vai sortear 5 numeros e vai colocalos dentro da lista e a segunda função vai mostrar a soma
# entre todos os valores pares sorteados pela função anterior.
# ======================================================================================================================
from random import randint
from time import sleep


def sorteia(num, limitebaixo, limitealto):
    print(f'sorteando {num} valores entre {limitebaixo} e {limitealto}:', end=' ', flush=True)
    sleep(2)
    for c in range(0, num):
        n = randint(limitebaixo, limitealto)
        print(n, end=' ', flush=True)
        numeros.append(n)
        sleep(.5)
    print()


def somaPar(lst):
    somaPares = 0
    print(f'na lista {numeros}, os numeros pares encontrados: ', end=' ', flush=True)
    sleep(2)
    for valor in lst:
        if valor % 2 == 0:
            print(valor, end=' ', flush=True)
            somaPares += valor
            sleep(.5)
    print(f'  somados é {somaPares}')


# PROGRAMA PRINCIPAL
numeros = []

sorteia(5, 1, 10)
somaPar(numeros)

# fim
input('aperte [enter] para sair')
