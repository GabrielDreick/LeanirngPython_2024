# ======================================================================================================================
# Crie um programa que faça o computador jogar JOKENPÔ com você.
# ======================================================================================================================
########################################################################################################################
import random

cores = {'': '\033[minutos',
         'y': '\033[1;33m'}

jokenpo = ['pedra', 'papel', 'tesoura']

print(f'vamos jogar {cores["y"]}Pedra Papel Tesoura{cores[""]}')

jogador = str(input(':')).strip().lower()
pc = random.choice(jokenpo)

perde = '\nEu Ganhei. mais sorte na proxima vez.'
ganha = '\nVocê Ganhou. Parabens'

if pc == 'pedra' and jogador == 'tesoura':
    print(pc, perde)
elif pc == 'tesoura' and jogador == 'papel':
    print(pc, perde)
elif pc == 'papel' and jogador == 'pedra':
    print(pc, perde)
elif jogador == 'pedra' and pc == 'tesoura':
    print(pc, ganha)
elif jogador == 'tesoura' and pc == 'papel':
    print(pc, ganha)
elif jogador == 'papel' and pc == 'pedra':
    print(pc, ganha)
elif pc == jogador:
    print(pc, '\nempate')
else:
    print('\033[7;30;41mnão previ isso...\033[minutos')
