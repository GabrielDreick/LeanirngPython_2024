# ======================================================================================================================
# Desenvolva um programa que leia o NOME, IDADE e SEXO de 4 PESSOAS. No final do programa, mostre:
#
# >A MEDIA DE IDADE do grupo
# >Qual é o nome do homem MAIS VELHO.
# >Quantas mulheres tem MENOS DE 20 anos.
# ======================================================================================================================
from time import sleep
vai = 0
tamanhoGrupo = int(input('Quantas pessoas tem no seu grupo? >'))

mediaIdade = 0
nomeHomemMaisVelho = ""
mulheresAbaixo20 = 0

if tamanhoGrupo == 0:                                     #
    print('zero? ')                                       #
    sleep(2)                                              #
    print('...zero...')                                   #
    sleep(5)                                              #
    print('\033[7;30;41m. . . Z E R O . . .\n\n\033[minutos')   #
elif tamanhoGrupo == 1:                                   #
    print('Ta sozinho é? ta bom, vamos la...\n')          #
    sleep(1)                                              #
    vai = 1                                               #
else:                                                     #
    vai = 1                                               #

if vai:
    for perfil in range(1, tamanhoGrupo+1):
        print('\n')
        nome = str(input('Qual é o seu nome? ')).strip()
        idade = int(input('Qual é sua idade? '))
        sexo = str(input('Qual é o seu sexo? [M/F] ')).strip()
        mediaIdade = mediaIdade + idade
        if sexo in 'Mm':
            if idade >= idade:
                nomeHomemMaisVelho = nome
        elif sexo in 'Ff':
            if idade < 20:
                mulheresAbaixo20 = mulheresAbaixo20 + 1
        else:
            print('mantenha simples')
        print('\n\n')

mediaIdade = mediaIdade / tamanhoGrupo
print(f'A media de idade do grupo é {mediaIdade:.2f}\n'
      f'O homem mais velho é o {nomeHomemMaisVelho.capitalize()}\n'
      f'Esse grupo tem {mulheresAbaixo20} mulheres com menos de vinte anos')

# fim
