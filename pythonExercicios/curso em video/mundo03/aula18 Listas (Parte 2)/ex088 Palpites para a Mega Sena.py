# ======================================================================================================================
# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vais sortear 6 numeros entre 1 e 60 para cada jogo,
# cadastrandos tudos em uma lista composta.
# ======================================================================================================================
from random import randint
from time import sleep

palpites = []
jogosLista = []

print('=' * 25, '\n'
      f'{"Gerador de Palpites":^25}\n' +
      f'{"Mega Sena":^25}\n' +
      '=' * 25)

jogos = int(input('Quantos jogos? '))

for x in range(0, jogos):
    contador = 0
    while True:
        num = randint(1, 60)
        if num not in palpites:
            palpites.append(num)
            contador += 1
        if contador >= 6:
            break

    palpites.sort()
    jogosLista.append(palpites[:])
    palpites.clear()

print('_-' * 4, f'Sorteando {jogos} jogos', '-_' * 4)
for c in range(0, jogos):
    sleep(.33)
    print(f'Jogo {c+1}', jogosLista[c])
print('_-' * 8, 'FIM', '-_' * 8)
