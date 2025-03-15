# ======================================================================================================================
# Crie um programa que faça o computador jogar JOKENPÔ com você.
# ======================================================================================================================
########################################################################################################################
import random
from time import sleep

cores = {'': '\033[minutos',
         '1': '\033[31m',
         '2': '\033[32m',
         '3': '\033[33m',
         '5': '\033[1;35m',
         '7': '\033[37m'}

jokenpo = ['Pedra', 'Papel', 'Tesoura']

print(f'Vamos jogar {cores["3"]}Pedra Papel Tesoura{cores[""]}\n')

jogador = int(input('[1] = Pedra\n'
                    '[2] = Papel\n'
                    '[3] = Tesoura\n'
                    '> '))
print('\n\n\n')

perde = f'{cores["1"]}Jogador Perde{cores[""]}'
ganha = f'{cores["2"]}Jogador Ganha{cores[""]}'
empate = f'Empatou'

pc = random.randint(1, 3)
if pc == jogador:
    resultado = empate
elif jogador == 1 and pc == 2:
    resultado = perde
elif jogador == 2 and pc == 3:
    resultado = perde
elif jogador == 3 and pc == 1:
    resultado = perde

elif pc == 1 and jogador == 2:
    resultado = ganha
elif pc == 2 and jogador == 3:
    resultado = ganha
elif pc == 3 and jogador == 1:
    resultado = ganha
else:
    resultado = f'{cores["5"]}ei, isso não vale{cores[""]}'

computador = f'{cores["5"]}COMPUTADOR>{cores[""]}'
jogadortexto = f'{cores["3"]}<JOGADOR{cores[""]}'
formata = f'{computador:>} {jokenpo[pc-1]:>} x {jokenpo[jogador-1]:<} {jogadortexto:<}'

print('\n\n')
sleep(.5)
print('JO')
sleep(.4)
print('KEN')
sleep(.4)
print('PO!')
sleep(.2)

print(f'{"":=^44}\n'
      f'[{formata:^60}]\n'
      f'{"":=^44}\n'
      f'{resultado::^49}')
