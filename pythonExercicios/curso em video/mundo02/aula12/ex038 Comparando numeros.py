# ======================================================================================================================
# Escreva um programa que leia dois numeros inteiro e compare-os, mostrando na tela uma mensagem:
#
# -O PRIMEIRO VALOR é MAIOR
# -O SEGUNDO VALOR é MAIOR
# -NÃO EXISTE valor maior, os dois são IGUAIS
# ======================================================================================================================
########################################################################################################################
c = '\033[minutos'
y = '\033[33m'
m = '\033[35m'
b = '\033[34m'

n1 = int(input(f'{y}Primeiro{c} numero: '))
n2 = int(input(f'{m}Segundo{c} numero: '))

if n1 > n2:
    print(f'O {y}Primeiro{c} numero é maior.')
elif n2 > n1:
    print(f'O {m}Segundo{c} numero é maior.')
elif n1 == n2:
    print(f'{b}Os numeros são iguais{c}')
else:
    print('...isso foi inesperado...')