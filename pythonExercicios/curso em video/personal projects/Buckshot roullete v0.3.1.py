from random import choice, randint
from time import sleep
from pygame import mixer

mixer.init()

C = {'': '\033[minutos',
     'hp': '\033[38;2;100;200;100m',
     'l': '\033[31m',
     'b': '\033[38;2;100;150;200m',
     '-': '\033[9;38;2;75;75;75m',
     'player': '\033[38;2;255;255;0m',
     'dealer': '\033[38;2;255;0;255m',
     'boom': '\033[38;2;255;175;100m',
     'click': '\033[38;2;150;150;150m'}  # COLORS

# TODO implement an item system for dealer

# ###### sound
shotClick = 'emptygunfire.mp3'
shotSelf = 'shotgunself.mp3'
shotGun = 'shotgunshot.mp3'
# ====== sound

turncount = turnkeep = loaded = 0
turn = 'playerturn'

dealerHp = playerHp = maxHp = 4
HP = f'{C["hp"]}█{C[""]}'

shellsList = []
itemList = ['cerveja', 'serra', 'lupa', 'cigarro', 'algemas']
playerItem = []
playerItemNew = ''  # to show when reloading
dealerItem = []
algemas = 0
dmg = 1

print('\n' * 30)
print('mostrar quantos cartuchos restam toda vez?\n')
sleep(2)
mostrarMunicao = str(input('[SIM](facil) apos cada turno, sera mostrado quantos cartuchos restam\n'
                           '[NAO](dificil) a quantidade de cartuchos so sera mostrado apos carregar a arma\n'
                           '>')).strip().upper()

while True:
# ########## RELOADING / ITENS ########################################################## RELOADING / ITENS ########## #
    if len(shellsList) == 0:
        loaded = 0
        mostrarMunicaoNao = 1
        print('RECARREGANDO', end='')
        sleep(.5)
        print('.', end=' ')
        sleep(.5)
        print('.', end=' ')
        sleep(.5)
        print('.')
        sleep(1)
        print('\n' * 30)

        print(f'você recebeu:', end=' ')
        if len(playerItem) < 8:
            for c in range(0, 2):
                playerItemNew = choice(itemList)
                print(f'{playerItemNew}', end='. ')
                playerItem.append(playerItemNew)
                if len(playerItem) >= 8:
                    break
        elif len(playerItem) >= 8:
            print('Itens demais.')

        if len(dealerItem) < 8:
            dealerItem.append(choice(itemList))
        print()

        sleep(2)
# ============================= RELOADING / ITENS ==================== RELOADING / ITENS ============================= #

    turncount += 1
    if turn == 'playerturn':
        print(f'{"":=^20}\n'
              f'{C["player"]}{"VEZ DO PLAYER":^20}{C[""]}\n'
              f'{"":=^20}')
    elif turn == 'dealerturn':
        print(f'{"":=^20}\n'
              f'{C["dealer"]}{"VEZ DO DEALER":^20}{C[""]}\n'
              f'{"":=^20}')


# HP ############################################################################################################## HP #
    DealerHP = HP * dealerHp
    PlayerHP = HP * playerHp
    print(f'{"Dealer":<6}|{"Player":>6} \n'
          f'{f"{DealerHP}":_<6}|{PlayerHP:>6}')
    print('=' * 30)
# HP ============================================================================================================== HP #
#
#
#
# AMMO ########################################################################################################## AMMO #
# ##### DEALING AMMO ############################################################################## DEALING AMMO ##### #
    if loaded == 0:
        x = 2
        maxammo = randint(2, 8)
        if maxammo > 4:
            x = 4
            shellsList.append('live')
            shellsList.append('blank')

        liv = f'{C["l"]}█{C[""]}'
        bla = f'{C["b"]}█{C[""]}'

        shellsList = ['live', 'blank']
        for c in range(0, maxammo - x):  # to pump a random shell each rotation                ### DEAL AMMO
            shell = randint(0, 1)
            if shell == 1:
                shellsList.append('live')
            else:
                shellsList.append('blank')
        loaded = 1
# ===== DEALING AMMO ============================================================================== DEALING AMMO ===== #
# ######################## PRINTING AMMO ###################################### PRINTING AMMO ######################## #
    if mostrarMunicao == 'NAO':
        mostrarMunicaoNao = 1
        mostrarMunicao = ''
    if mostrarMunicao == 'SIM' or mostrarMunicaoNao == 1:

        if turncount < 3:
            if shellsList.count('live') > 1:
                print(f'{C["l"]}{shellsList.count("live")} Cartuchos Cheios{C[""]}')
            else:
                print(f'{C["l"]}{shellsList.count("live")} Cartucho Cheio{C[""]}')
            if shellsList.count('blank') > 1:
                print(f'{C["b"]}{shellsList.count("blank")} Cartuchos Vazios{C[""]}')
            else:
                print(f'{C["b"]}{shellsList.count("blank")} Cartucho Vazio{C[""]}')
            print('')

        for c in range(0, len(shellsList)):  # CHECK THEN PRINT
            if shellsList[c] == 'live':
                print(liv, end='')
            elif shellsList[c] == 'blank':
                print(bla, end='')
        print()
        print('=' * 30)
        mostrarMunicaoNao = 0
# ======================== PRINTING AMMO ====================================== PRINTING AMMO ======================== #
# AMMO ========================================================================================================== AMMO #
#
#
#
# ACTION ###################################################################################################### ACTION #
# ############### PLAYER'S TURN ######################################################## PLAYER'S TURN ############### #
    shot = choice(shellsList)

    if turn == 'playerturn':
        act = ''
        itemChoose = -1
        while act == '':
            while act != 'ATIRAR' and act != 'ITEM':
                act = str(input(f'{"O que você faz?":^24}\n'
                                f'[ATIRAR]\n'
                                f'[ITEM] (WIP)\n'
                                f'{">":>8}')).strip().upper()
# ############### PLAYER SHOOTS ######################################################## PLAYER SHOOTS ############### #
            if act == 'ATIRAR':
                shoot = ''
                while shoot != 'DEALER' and shoot != 'PLAYER':
                    shoot = str(input(f'Em quem você atira?\n'
                                      f'[{C["dealer"]}DEALER{C[""]}] ou [{C["player"]}PLAYER{C[""]}]\n'
                                      f'{">>":>7}')).strip().upper()

                sleep(.5)
                print('.', end=' ')
                sleep(.5)
                print('.', end=' ')
                sleep(.5)
                print('.')
                sleep(1)
                print('\n' * 30)


# ============================== PLAYER SHOOTS ========================== PLAYER SHOOTS ============================== #
# ############### PLAYER ITEM ############################################################ PLAYER ITEM ############### #
            if act == 'ITEM':
                while True:
                    itemChoose = 98463
                    while itemChoose not in range(0, len(playerItem)) and itemChoose != 10:

                        print('\n' * 30)
                        print(f'[-1] voltar')
                        for c in range(0, len(playerItem)):
                            print(f'[{c}] {playerItem[c]}')

                        print('[10] Descrição dos Itens')

                        itemChoose = int(input('>>'))

                        if itemChoose == -1:
                            break
                    if itemChoose == -1:
                        act = ''
                        break

                    elif itemChoose == 10:
                        print('Cerveja: Descarta o cartucho na camara. termina a rodada se esvaziar a arma.\n'
                              'Serra: O proximo cartucho ira dar dano duplo.\n'
                              'Algemas: Mantem o turno.\n'
                              'Lupa: Revela o cartucho carregado na camara.\n'
                              'Cigarro: Recupera um ponto de vida. não excede a vida maxima.')
                        input('[voltar]')

                    else:
                        itemUse = playerItem[itemChoose]
                        playerItem.remove(itemUse)

                    if itemChoose == 10:
                        pass
                    elif itemUse == 'cerveja':            # cerveja
                        if len(shellsList) > 1:
                            if shot == 'live':
                                print(liv, 'descartado')
                            elif shot == 'blank':
                                print(bla, 'descartado')
                            shellsList.remove(shot)
                            shot = choice(shellsList)
                        elif len(shellsList) <= 1:
                            print('so tem uma na camara, nao codei pra recarregar')

                    elif itemUse == 'lupa':             # lupa
                        if shot == 'live':
                            print(liv)
                        elif shot == 'blank':
                            print(bla)

                    elif itemUse == 'serra':            # serra
                        dmg = 2
                        print('dano x2')

                    elif itemUse == 'cigarro':          # cigarro
                        if playerHp < maxHp:
                            print(f'Player HP: {HP * playerHp}', end='')
                            playerHp += 1
                            sleep(1)
                            print(HP)

                    elif itemUse == 'algemas':          # algemas
                        turnkeep += 1
                        print('Prendeu o Dealer por um turno')

                    sleep(2)

                    if len(shellsList) < 1:
                        break
                if len(shellsList) < 1:
                    break
            if len(shellsList) < 1:
                break

# ============================== PLAYER'S ITEM ========================== PLAYER'S ITEM ============================== #
# ============================== PLAYER'S TURN ========================== PLAYER'S TURN ============================== #
# ########## DEALER'S TURN ################################################################## DEALER'S TURN ########## #
    elif turn == 'dealerturn':
        sleep(2)

        dealerAction = ['shoot']
        if len(dealerItem) > 0 and 'item' not in dealerAction:
            dealerAction.append('item')
        elif len(dealerItem) == 0 and 'item' in dealerAction:
            dealerAction.remove('item')

        dealerShoot = []        # who will the dealer shoot
        for c in shellsList:
            if c == 'live':
                dealerShoot.append('PLAYER')
            elif c == 'blank':
                dealerShoot.append('DEALER')

        shoot = choice(dealerShoot)

        sleep(1)
        if shoot == 'PLAYER':
            print(f'{C["dealer"]}Dealer{C[""]} atira em {C["player"]}Player{C[""]}')
        elif shoot == 'DEALER':
            print(f'{C["dealer"]}Dealer{C[""]} atirar em {C["dealer"]}Dealer{C[""]}')
        sleep(1)
        print('.', end=' ')
        sleep(.5)
        print('.', end=' ')
        sleep(.5)
        print('.')
        sleep(1)
        print('\n' * 30)

# ############### DEALER ITEM ############################################################ DEALER ITEM ############### #
        '''if dealerAct == 'ITEM':
            while True:
                itemChoose = 98463
                while itemChoose not in range(0, len(playerItem)):

                    print('\n' * 30)
                    print(f'[-1] voltar')
                    for c in range(0, len(playerItem)):
                        print(f'[{c}] {playerItem[c]}')

                    itemChoose = int(input('>>'))

                    if itemChoose == -1:
                        break
                if itemChoose == -1:
                    act = ''
                    break

                itemUse = playerItem[itemChoose]
                playerItem.remove(itemUse)

                if itemUse == 'cerveja':  # cerveja
                    if shot == 'live':
                        print(liv, 'descartado')
                    elif shot == 'blank':
                        print(bla, 'descartado')
                    shellsList.remove(shot)
                    shot = choice(shellsList)

                elif itemUse == 'lupa':  # lupa
                    if shot == 'live':
                        print(liv)
                    elif shot == 'blank':
                        print(bla)

                elif itemUse == 'serra':  # serra
                    dmg = 2
                    print('dano x2')

                elif itemUse == 'cigarro':  # cigarro
                    if playerHp < maxHp:
                        playerHp += 1
                    print(f'Player HP: {HP * playerHp}')

                elif itemUse == 'algemas':  # algemas
                    turnkeep = 1

                sleep(2)'''
# ============================== DEALER'S ITEM ========================== DEALER'S ITEM ============================== #
# ============================== DEALER'S TURN ========================== DEALER'S TURN ============================== #
# ########## SHOOTING ############################################################################ SHOOTING ########## #
    if shot == 'live':
        mixer.music.load(shotGun)
        if shoot == 'PLAYER':
            mixer.music.load(shotSelf)
            mixer.music.play()
            playerHp -= dmg
            print(f'{C["boom"]}bo-{C[""]}')

        elif shoot == 'DEALER':
            mixer.music.play()
            dealerHp -= dmg
            print(f'{C["boom"]}boom{C[""]}')

    elif shot == 'blank':
        mixer.music.load(shotClick)
        if shoot == 'PLAYER':
            mixer.music.play()
            print(f'{C["click"]}click{C[""]}', end=' ')
            if turn == 'playerturn':
                print('mantem a vez')
                turnkeep += 1

        elif shoot == 'DEALER':
            mixer.music.play()
            print(f'{C["click"]}click{C[""]}', end=' ')
            if turn == 'dealerturn':
                print('mantem a vez')
                turnkeep += 1

        print()
    shellsList.remove(shot)
    if dmg == 2:
        print('dano x1')
        dmg = 1
    sleep(2)
    print('\n' * 30)

    if turnkeep > 0:
        turnkeep = 0
    else:
        if turn == 'playerturn':
            turn = 'dealerturn'
        elif turn == 'dealerturn':
            turn = 'playerturn'
# ============================== SHOOTING ===================================== SHOOTING ============================= #
# ACTION ====================================================================================================== ACTION #

    if playerHp <= 0 or dealerHp <= 0:
        break
if playerHp > 0:
    print('voce venceu')
elif dealerHp > 0:
    for c in '...........':
        sleep(.35)
        print(c)
