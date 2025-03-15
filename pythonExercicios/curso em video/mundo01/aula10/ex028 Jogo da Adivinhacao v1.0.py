from random import randint
from time import sleep
'''
====================[Desafio028]====================
Escreva um programa que faça o computador "pensar"
em um numero inteiro entre 0 e 5 e peça para o 
usuario tentar descobrir qual foi o numero
escolhido pelo computador.

O programa devera escrever na tela se o usuario
venceu ou perdeu.
====================================================
'''
########################################################################################################################
########################################################################################################################
n1 = 0
n2 = 5
n = randint(n1, n2)
num = int(input('\n'
                '          (0 ate 5)\n'
                'Em que numero estou pensando?'))
print('...')
sleep(2)
print('...Você...')
sleep(2)
if num == n:
    print('       ...ACERTOU!!!')
else:
    print('       ...errou...')
    sleep(1)
    print(f'eu pensei no numero {n}. mais sorte na proxima vez.')
sleep(1)
