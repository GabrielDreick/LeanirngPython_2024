# ======================================================================================================================
# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma do valores da terceira coluna.
# C) O maior valor da segunda linha.
# ======================================================================================================================
matriz = [[], [], [], [], [], [], [], [], []]
contador = somaPar = somaTerceira = maior = 0
for c in range(0, 9):
    contador += 1
    num = int(input(f'{contador}º valor: '))
    matriz[c].append(num)

    if num % 2 == 0:
        somaPar += num

    if contador % 3 == 0:
        somaTerceira += num

    if str(contador) in '456':
        if num > maior:
            maior = num

print(f'{matriz[0:3]}\n'
      f'{matriz[3:6]}\n'
      f'{matriz[6:9]}')

print(f'a soma de todos os valores pares dá {somaPar}\n'
      f'a soma dos valores da terceira coluna dá {somaTerceira}\n'
      f'e o maior valor da segunda linha é {maior}')

# fim do meu

par = somaCol = mai = 0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Posição[{linha}:{coluna}] Digite um valor: '))

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
        if matriz[linha][coluna] % 2 == 0:
            par += matriz[linha][coluna]
    print()

for linha in range(0, 3):
    somaCol += matriz[linha][2]

for coluna in range(0, 3):
    if coluna == 0:
        mai = matriz[1][coluna]
    elif matriz[1][coluna] > mai:
        mai = matriz[1][coluna]

print(f'a soma de todos os valores pares dá {par}\n'
      f'a soma dos valores da terceira coluna dá {somaCol}\n'
      f'e o maior valor da segunda linha é {mai}')

# fim do Gustavo
