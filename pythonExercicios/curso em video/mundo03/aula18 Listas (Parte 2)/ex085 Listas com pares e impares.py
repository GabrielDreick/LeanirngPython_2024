# ======================================================================================================================
# Crie um programa onde o usuario pode digitar sete valores numericos e cadastre-os em uma lista unica que mantenha
# separados os valores pares e impares.
# No final, mostre os valores pares e impares em ordem crescente.
# ======================================================================================================================
numeros = [[], []]
for c in range(0, 7):
    num = int(input('Numero: '))
    if num % 2 == 0:
        numeros[0].append(num)
    elif num % 2 != 0:
        numeros[1].append(num)
numeros[1].sort()
numeros[0].sort()
print(f'Numeros pares: {numeros[0]}\n'
      f'Numeros impares: {numeros[1]}')

# fim
input('aperte [enter] para sair')
