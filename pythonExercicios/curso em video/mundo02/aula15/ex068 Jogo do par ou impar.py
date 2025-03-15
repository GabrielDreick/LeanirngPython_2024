# ======================================================================================================================
# Faça um programa que joge par ou impar com o computador.
# O jogo so sera interrompido quando o jogador PERDER,
# mostrando o total de vitorias consecutivas que ele conquistou no final do jogo.
# ======================================================================================================================
from random import randint

print('Agora no vamos jogar ´´Par ou Impar``, o jogo so acaba quando voce perder. \033[38;2;60;60;60mvai ser rapido\033[0m')
consecutivas = soma = 0
while True:
    playerPoI = ''
    while playerPoI != 'P' and playerPoI != 'I':
        playerPoI = str(input('Par ou Impar [P/I]? ')).strip().upper()
    playerNum = int(input('Numero: '))
    pc = randint(0, 10)
    print(pc)
    soma = pc + playerNum
    if playerPoI == 'I' and soma % 2 != 0:
        consecutivas += 1
    elif playerPoI == 'P' and soma % 2 == 0:
        consecutivas += 1
    else:
        break
    if consecutivas <= 2:
        print('denovo...¬¬')
    elif consecutivas >= 3:
        print('DENOVO ֎`_´֍')

    print(f'{consecutivas}  vitoria consecutivas')
print('fim.euganho voceperde.euvenci.voceperdeu.tchau.')

# fim
