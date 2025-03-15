# ======================================================================================================================
# Crie um programa que tenha um tupla totamente preenchida com uma contagem por extenso, de zero a vinte.
# Seu programa devera ler um numero pelo teclado (entre 0 e 20) e mostra-la por extenso.
# ======================================================================================================================
from time import sleep

extenso = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove',
           'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove',)
dezena = ('use o 2', 'use o 2', 'vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa')

print('oh, olá.')
sleep(.34)
while True:
    num = -1
    while num < 0 or num > 99:
        num = int(input('\nPor favor, digite um numero entre 0 e 20: '))
        sleep(.56)
        if num == -999:     # SAIDA
            break           # SAIDA
        if num < 0 or num > 99:
            print('Meu criador não fez algo para esse numero\n')
    if num == -999:         # SAIDA
        sleep(1.31)
        break               # SAIDA
    if 0 <= num < 20:
        print(f'Áh, você ta falando do \033[33m{extenso[num]}\033[0m')
    elif num % 10 == 0:
        print(f'Áh, o numero \033[33m{dezena[num // 10]}\033[0m')
    elif num > 20:
        print(f'Áh, o numero \033[33m{dezena[num // 10]} e {extenso[num % 10]}\033[0m')

print('voce esta indo embora? tchau.')
