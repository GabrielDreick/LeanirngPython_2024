# ======================================================================================================================
# Faça um program que tenha uma função chamada contador(),
# que receba três parametros:
# inicio, fim e passo, e realize a contagem.
#
# seu programa tem que realizar três contagens atraves da função criada:
#
# A) De 1 até 10, de 1 em 1
# B) De 10 até 0, de 2 em 2
# C) Uma contagem personalizada
# ======================================================================================================================
from time import sleep


def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
        print('passo não pode ser 0, devolvendo pra 1')
    print(f'Começando no numero {inicio} ate o numero {fim} pulando de {passo} em {passo}')
    sleep(5)
    for c in range(inicio, fim, passo):
        print(c, end=' ')
        sleep(.21)
    print()


contador(1, 10, 1)
contador(10, 0, -2)
contador(int(input("Numero de Inicio: ")),
         int(input("Numero Final: ")),
         int(input("A que Passo: ")))

# f
