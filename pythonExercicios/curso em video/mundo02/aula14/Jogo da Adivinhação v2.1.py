from random import randint
from time import sleep
from pygame import mixer
mixer.init()

c = {'': '\033[0m',
     'p': '\033[7;30;48;2;172;0;75m',
     '#': '\033[38;2;255;255;255m',
     'W': '\033[38;2;75;200;75m',
     'L': '\033[38;2;200;50;50m'}

game = 1
while game == 1:

    print('\n' * 30)
    pc = randint(0, 10)
    player = -1
    tentativa = 3
    print(f'\n'
          f'{c["#"]}Eu pensei em um numero de 0 a 10, tente adivinhar com apenas {tentativa} tentativas{c[""]}\n')

    while player != pc and tentativa > 0:
        print(f'{c["p"]}[{tentativa}] tentativas restantes{c[""]}')
        player = int(input())
        tentativa -= 1
        sleep(.5)
        print('.')
        sleep(.5)
        print('. .')
        sleep(.5)
        print('. . .')
        sleep(1)
        if player > pc and tentativa > 0:
            print('mais baixo...')
        elif player < pc and tentativa > 0:
            print('mais alto...')

    if player == pc:
        mixer.music.load('victory.mp3')
        print('\n' * 30)
        mixer.music.play()
        print(f'\n{c["W"]}Acertou{c[""]}')
    elif player != pc:
        mixer.music.load('sad-trombone.mp3')
        mixer.music.play()
        print('\n' * 30)
        print(f'{c["L"]}eu tinha pensado no numero {pc}\n'
              f'Não foi desta vez...{c[""]}')
    sleep(1)
    play = ''
    while play != 'S' and play != 'N':
        play = str(input('Jogar novamente [S/N]? ')).strip().upper()
        if play == 'S':
            game = 1
        elif play == 'N':
            game = 0
# fim
