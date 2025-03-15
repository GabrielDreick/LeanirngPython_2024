# ======================================================================================================================
# Crie um programa que vai gerar cinco numero aleatorios e colocar em uma tupla.
#
# Depois disso, mostre a listagem de numeros gerados e tambem indique o menor e o maior valor que estão na tupla.
# ======================================================================================================================
from random import randint
from time import sleep

aleatorios = (randint(1, 9999), randint(1, 9999), randint(1, 9999), randint(1, 9999), randint(1, 9999))
print('ola, bom te ver \033[38;2;100;100;100m(mesmo que eu não consiga de verdade.)\033[0m')
sleep(2)
print('usei meu aleatorizador para pensar em cinco numeros aleatorios')
sleep(2)
print('aqui estão:')
for c in range(0, len(aleatorios)):
    print(aleatorios[c], end=' ')
'''    if c == 0:
        maior = aleatorios[c]
        menor = aleatorios[c]
    elif aleatorios[c] > maior:
        maior = aleatorios[c]
    elif aleatorios[c] < menor:
        menor = aleatorios[c]

print(f'\ne o maior numero daquela lista é o numero {maior}\n'
      f'e o menor é o numero {menor}\n')
'''  # depreciado
print(f'\ne o maior numero daquela lista é o numero {max(aleatorios)}\n'
      f'e o menor é o numero {min(aleatorios)}')
sleep(1)
print('bom, é isso.', end=' ')
sleep(.21)
print('tchau.')
sleep(.5)

# fim
