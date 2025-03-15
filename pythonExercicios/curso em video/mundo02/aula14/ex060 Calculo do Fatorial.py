# ======================================================================================================================
# Faça um programa que leia um numero qualquer e mostre o sei fatorial.
#
# Ex:
# 5! = 5 * 4 * 3 * 2 * 1 = 120
# ======================================================================================================================
from math import factorial
print('Vou te mostrar o fatorial do seu numero (5! = 5 x 4 x 3 x 2 x 1 = 120)')
num = int(input('Digite um numero qualquer: '))
c = num
factor = 1
while c > 0:
    factor = factor * c
    c = c - 1

'''
if num == 1:
    x = 0
    factor = 1
else:
    x = num - 1
    factor = 0

while x > 0:
    if x == num - 1:
        factor = num * x
        x = x - 1
    else:
        factor = factor * x
        x = x - 1
'''
print(f'O fatorial de {num} é {factor}')

# fim
