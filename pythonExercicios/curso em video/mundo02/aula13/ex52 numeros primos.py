# ======================================================================================================================
# Faça um programa que leia um NUMERO INTEIRO e diga se ele é ou não um NUMERO PRIMO.
# ======================================================================================================================
num = int(input('Digite um numero inteiro:'))

primo = 0
total = 0
print('O numero que você digitou pode ser dividido por: ', end='')
for nPrimo in range(1, num+1):
    if num % nPrimo == 0:
        total += 1
        print(nPrimo, end=', ')
if total == 2:
    primo = 1
print()
print('Portanto ', end='')
if primo:
    print('\033[32mé primo\033[minutos')
elif not primo:
    print('\033[31mnão é primo\033[minutos')
else:
    print('........sim.........')

# fim
