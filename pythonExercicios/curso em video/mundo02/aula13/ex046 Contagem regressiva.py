# ======================================================================================================================
# Faça um programa que mostre na tela uma CONTAGEM REGRESSIVA para o estouro de fogos de artificio, indo de 10 ATE 0,
# com uma pausa de 1 SEGUNDO entre eles.
# ======================================================================================================================
from time import sleep

c = {'0': '\033[ml',
     '3': '\033[33m',
     '1': '\033[31m',
     '5': '\033[35m'}

for contagem in range(40, 0, -1):
    if contagem > 9:
        k = c["0"]
    if 3 < contagem < 6:
        k = c["3"]
    if contagem <= 35:
        k = c["1"]
    print(f'{k}{contagem}')
    sleep(1)
print(f'{c["5"]}(fogos de artificio explodindo super epicamente)')

# fim
