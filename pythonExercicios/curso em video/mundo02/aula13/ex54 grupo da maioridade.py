# ======================================================================================================================
# Crie um programa que leia o ANO DE NASCIMENTO de SETE PESSOAS.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
# considerando maioridade sendo 21 anos
# ======================================================================================================================
from datetime import date
hoje = date.today().year

maior = 0
menor = 0

for c in range(0, 7):
    ano = int(input(f'{c+1}º Ano de nascimento: '))
    if hoje - ano >= 21:
        maior = maior + 1
    elif hoje - ano < 21:
        menor = menor + 1
    else:
        print('...estranho...')

print(f'{maior} pessoas são maiores de idade\n'
      f'{menor} pessoas são menores de idade')

# fim
