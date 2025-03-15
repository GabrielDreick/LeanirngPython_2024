# ======================================================================================================================
# Faça um programa que leia o PESO de CINCO PESSOAS. No final, mostre qual foi o MAIOR e MENOR peso lidos.
# ======================================================================================================================
'''
maior = 0
menor = 0
'''
maior = 0
menor = 0

for pesos in range(1, 6):
    peso = float(input(f'{pesos}º peso:'))
    if pesos == 1:                         # Gustavo disse que pessoas usam gambiarra: menor = 999999, se num < menor
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso

print(f'O mais pesado é {maior:.2f}Kg\n'
      f'O mais leve é {menor:.2f}Kg')

# fim
