# ======================================================================================================================
# Melhore jogo do DESAFIO 028 onde o computador voi  pensar em um numero entre 0 e 10.
# só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.
# ======================================================================================================================
from random import randint, choice

c = {'': '\033[0m',
     '0': '\033[38;2;100;100;100m',
     '3': '\033[38;2;255;255;0m',
     'br': '\033[38;2;150;75;50m',
     'or': '\033[38;2;200;150;50m'}

naoLista = ['Não é esse', f'{c["or"]}É outro numero{c[""]}...', f'{c["br"]}outro{c[""]}',
            f'{c["3"]}É O NUMERO{c[""]}- {c["0"]}quase estraguei o jogo.{c[""]}']

print('vou pensar em um numero de 0 ate 10 e sera o mesmo numero ate você acertar')
pc = randint(0, 10)
num = -1
palpite = 0
while num != pc:
    num = int(input('>>'))
    palpite += 1
    if -1 < num < 11:
        if num != pc:
            print(choice(naoLista))
    else:
        print(f'eu disse de 0 até 10, {num} esta fora desse alcance')
if num == pc:
    if palpite == 1:
        print('Acertou de primeira')
    else:
        print(f'Acertou, e tentou {palpite} vezes')
else:
    print('\033[1;7;30;48;2;255;0;0mCOMO VOCÊ SAIU DE LA?\n\n')

# fim
