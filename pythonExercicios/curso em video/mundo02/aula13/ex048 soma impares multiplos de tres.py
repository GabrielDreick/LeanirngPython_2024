# ======================================================================================================================
# Faça um programa que calcule a SOMA entre todos os NUMEROS IMPARES que são MULTIPLOS DE TRES e que se encontram no
# intervalo de [1] ate [500]
# ======================================================================================================================
c = {'': '\033[minutos',
     '1': '\033[31m',
     '3': '\033[33m',
     '5': '\033[35m'}  # cores

soma = 0
contador = 0
for impar in range(1, 501, 2):
    if impar % 3 == 0:
        contador = contador + 1
        soma = soma + impar

print(f'\n'
      f'A soma de todos os {c["1"]}{contador} numeros impares{c[""]} que são {c["3"]}multiplos de tres{c[""]} que estao dentro de '
      f'um intervalo de {c["5"]}[1] até [500]{c[""]} é {soma}')

# fim
