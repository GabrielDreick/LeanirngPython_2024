# ======================================================================================================================
# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
# no final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram o numero pares.
# ======================================================================================================================
from time import sleep

'''print('ola')
sleep(.75)
print('eu vou te pedir quatro numeros, e depois vou te dizer algumas informações predeterminadas sobre elas.')
sleep(4.86)
print('ta bom, vamos lá.')
sleep(1.14)'''
teclado4 = (int(input('primeiro numero: ')),
            int(input('segundo numero: ')),
            int(input('terceiro numero: ')),
            int(input('quarto numero: ')))
print(teclado4)

print(f'o valor ´´9`` apareceu {teclado4.count(9)} vez(es)')
if 3 in teclado4:
    print(f'o valor ´´3`` apareceu na {teclado4.index(3) + 1}ª posição')
else:
    print('você não digitou o valor ´´3``')
print('e o valores pares que você digitou são:')
for par in teclado4:
    if par % 2 == 0:
        print(par, end=' ')
