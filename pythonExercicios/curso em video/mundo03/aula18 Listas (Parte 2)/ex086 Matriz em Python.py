# ======================================================================================================================
# Crie um program que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
#      0   1   2
#    ┌───┬───┬───┐
#  0 │   │   │   │
#    ├───┼───┼───┤
#  1 │   │   │   │
#    ├───┼───┼───┤
#  2 │   │   │   │
#    └───┴───┴───┘
#
# No final, mostre a matriz na tela, com a formatação correta.
# ======================================================================================================================
matriz = [[], [], [], [], [], [], [], [], []]
for c in range(0, 9):
    num = input('valor: ')
    matriz[c].append(num)
print(f'[{matriz[0][0]:^4}] [{matriz[1][0]:^4}] [{matriz[2][0]:^4}]\n'
      f'[{matriz[3][0]:^4}] [{matriz[4][0]:^4}] [{matriz[5][0]:^4}]\n'
      f'[{matriz[6][0]:^4}] [{matriz[7][0]:^4}] [{matriz[8][0]:^4}]')

# fim do meu

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Posição[{linha}:{coluna}] Digite um valor: '))

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()

# fim do Gustavo
