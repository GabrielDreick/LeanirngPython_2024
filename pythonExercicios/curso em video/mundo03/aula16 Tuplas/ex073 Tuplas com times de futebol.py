# ======================================================================================================================
# Crie uma tupla preenchida com os 20 primeiros colocados na Tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação. Depois mostre:
#
# A) Apenas os 5 primeiros colocados.
# B) Os ultimos 4 colocados da tabela.
# C) Uma lista com os times em ordem alfabetica.
# D) Em que posição na tabela esta o time da Chapecoense
# ======================================================================================================================
from time import sleep
brasileirao = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo', 'Atlético-MG', 'Athletico-PR',
               'Cruzeiro', 'Botafogo', 'Santos', 'Bahia', 'Fluminense', 'Corinthians', 'Chapecoense', 'Ceará SC',
               'Vasco da Gama', 'Sport Recife', 'América-MG', 'EC Vitória', 'Paraná')

print('===========================\n'
      'tabela do Brasileirão: 2018\n'
      '===========================\n')
sleep(1)
print('Os primeiros 5 colocado são:')
for primeiros in range(0, 5):
    sleep(.5)
    print(f'-{brasileirao[primeiros]}')
sleep(.5)
print('...\n')

sleep(2)
print('Os ultimos 4 colocados são:')
for ultimos in range(len(brasileirao) - 4, len(brasileirao)):
    sleep(.25)
    print(f'-----{brasileirao[ultimos]}')
sleep(.5)
print('...\n')

sleep(2)
print('Todos em ordem alfabetica:')
sleep(1)
for alfa in range(0, len(brasileirao)):
    sleep(.21)
    print(f'{sorted(brasileirao)[alfa]}')
sleep(.5)
print('...\n')

sleep(3)
print(f'Chapecoense esta na posição n{brasileirao.index("Chapecoense") +1 }º')

# fim
