# ======================================================================================================================
# Crie um programa onde 4 jogadore joguem um dado e tenham resultados aleatorios.
# Guarde esses resultados em um dicionario.
# No final, coloque esse dicionario em ordem, sabendo que o vencedor tirou o maior numero no dado.
# ======================================================================================================================
from time import sleep
from random import randint
from operator import itemgetter

jogo = {}
for c in range(0, 4):
    jogo[f'jogador{c+1}'] = randint(1, 6)

ranking = []

x = .21
for k, v in jogo.items():
    print(f'{k} jogou o dado:', end=' ')
    sleep(x * 5)
    print(v)
    sleep(x)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
sleep(x * 5)

print('\n\n\n')
print('=' * 60)
for i, v in enumerate(ranking):
    print(f'{i+1}º Lugar: {v[0]} que rolou o numero {v[1]}')
    sleep(x)

# fim
