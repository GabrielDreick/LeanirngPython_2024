import pygame.mixer
pygame.init()
print('\n')

#                  11111111112
#        012345678901234567890
frase = 'Curso em Video Python'  # [x:y:z] x = start, y = stop before, z = jump
print(frase[9:13])               # >>Vide
print(frase[9:21:2])             # >>VdoPto
print(frase[:5])                 # >>Curso
print(frase[15:])                # >>Python
print(frase[9::3])               # >>VePh
print(frase[21:0:-1])
print()
print(len(frase))
print(frase.count('o', 0, 13))   # contando dentro de limites
print(frase.find('deo'))         # qual posiçao começa 'deo'
print(frase.find('Android'))     # -1 Nao Encontrado, continuando...
print('Curso' in frase)          # existe ou nao: True ou False
print(frase.replace('Python', 'Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print()
frase = '   Aprenda Python  '
print('-', frase, '-')
print('-', frase.strip(), '-')
print('-', frase.rstrip(), '-')
print('-', frase.lstrip(), '-')

frase = 'Curso em Video Python'
print(frase.split('o'))          # .split('o') corta(eliminando) cada 'o' >>['Curs', ' em Vide', ' Pyth', 'n']
print("HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")
print('-'.join(frase.split()))   # '-'.join(frase) >>C-u-r-segundos-o- -e-minutos-... .join(frase.split()) >>Curso-em-Vi...
print(frase.upper().count('O'))  # trasforma em MAIUSCULA e conta todos os 'O'

frase = '   Curso em Video Python   '
print(len(frase.strip()))        # conta quantos caracteres tem, depois de eliminar os espaços antes e depois
frase = 'Curso em Video Python'
frase = frase.replace('Python', 'Android')
print(frase)
dividido = frase.split()
print(dividido[3][2])

print('''
ai, da pra escrever
assim que funciona
sem problemas''')

########################################################################################################################
########################################################################################################################
print('\n'
      '========================================================================\n'
      'ex202: Crie um Programa que Leia o Nome Completo de uma Pessoa e Mostre:\n'
      '')

msg = input('M E N S A G E M : ')
n1 = int(input('C O D I G O   1 :'))
n2 = int(input('C O D I G O   2 :'))
n3 = int(input('C O D I G O   3 :'))
if n2 == 0:
    print(f'ERR#R##12#: [{msg[n1::n3]}]')
else:
    print(f'ERROR N121: [{msg[n1:n2:n3]}]')
input('[enter]')
print('\n'
      '\n'
      '\n'
      '\n'
      '\n'
      '\n'
      '\n'
      '\n'
      '\n'
      '\n'
      '\n'
      '\n'
      '\n'
      '\n'
      '\n'
      '\n'
      '\n'
      '\n'
      '\n'
      '\n'
      '\n'
      '\n'
      '\n'
      '\n'
      '\n'
      '')
passcode = input('S E N H A :')
password = '22 reu rgaaqeLi  oeCmlt euaPso  ote'

if passcode == password:
    print('C O R R E T O')
    input('[enter]')
else:
    print('I N C O R R E T O \n'
          '')
    pygame.mixer.music.load('emptygunfire.mp3')
    pygame.mixer.music.play()
    input('(o que foi iss-)\n'
          '[enter]')

    pygame.mixer.music.load('shotgunself.mp3')
    pygame.mixer.music.play()
    input('\n'
          '\n'
          '\n'
          '...[enter]...')
