# ======================================================================================================================
# Crie um programa que leia uma FRASE qualquer e diga se ela PALINDROMO, desconsiderando os espaços.
#
# Ex:
# APOS A SOPA
# ======================================================================================================================
print(' Vou te dizer se a frase que você digitar é um palindromo (lido igual de tras pra frente)')
frase = str(input('Digite uma frase: ')).upper()
inverso = ''
frase = frase.replace(' ', '')
'''
inverso = frase[::-1]
'''
for letra in range(len(frase)-1, -1, -1):
    inverso = inverso + frase[letra]
print('\n'
      f'{frase} {inverso}')
if inverso == frase:
    print('É um palindromo')
else:
    print('Não é um palindromo')
'''
frase = frase.replace(" ", "")
tamanho = len(frase)
selecao = -1
selecaofin = tamanho

diferente = 0
for comparar in range(tamanho // 2, tamanho + 1):
    selecao = selecao + 1
    selecaofin = selecaofin - 1
    if frase[selecao] != frase[selecaofin]:
        diferente = 1

if not diferente:
    print('É um palindromo')
else:
    print('Não é um palindromo')
'''
# fim
