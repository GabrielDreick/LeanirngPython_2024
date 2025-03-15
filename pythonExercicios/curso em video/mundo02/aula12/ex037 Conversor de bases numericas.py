# ======================================================================================================================
# Escreva um programa que leia um numero inteiro qualquer e peça para o usuario escolher qual sera a BASE DE CONVERSÃO
# - 1 para Binario
# - 2 para Octal
# - 3 para Hexadecimal
# ======================================================================================================================
########################################################################################################################
c = {'': '\033[minutos',
     '3': '\033[33m',
     '4': '\033[34m',
     '5': '\033[35m'}

print('Coversor de base numerica')
decimal = int(input('Me de um numero inteiro: '))

conversao = int(input('Para qual base numerica você quer converter?\n'
                      f'    {c["4"]}Binario{c[""]} = [1]\n'
                      f'      {c["5"]}Octal{c[""]} = [2]\n'
                      f'{c["3"]}Hexadecimal{c[""]} = [3]\n'
                      '>'))

if conversao == 1:
    binario = bin(decimal)
    print(f'Decimal: {decimal}\n'
          f'{c["3"]}Binario{c[""]}: {binario[2:]}')
elif conversao == 2:
    octal = oct(decimal)
    print(f'Decimal: {decimal}\n'
          f'{c["5"]}Octal{c[""]}: {octal[2:]}')
elif conversao == 3:
    hexadecimal = hex(decimal)
    print(f'Decimal: {decimal}\n'
          f'{c["3"]}Hexadecimal{c[""]}: {hexadecimal[2:]}')
else:
    print('ERR.ERR.ERR.ERR.ERR.ER-')
