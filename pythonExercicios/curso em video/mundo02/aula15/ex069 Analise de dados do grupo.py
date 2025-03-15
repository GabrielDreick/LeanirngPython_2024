# ======================================================================================================================
# Crie um programa que leia a idade eo sexo de varias pessoas.
# A cada pessoa cadastrada, o programa devera perguntar se o usuario quer ou não continuar.
# No final, mostre:
#
# A) quantas pessoas tem mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres tem menos de 20 anos.
# ======================================================================================================================
idade = mais18 = mulherMenos20 = homem = 0
while True:
    sexo = continuar = ''
    print('┌──────────────────┐\n'
          '│     CADASTRO     │\n'
          '├──────────────────┘')
    idade = int(input('╞Idade: '))
    if idade > 18:
        mais18 += 1
    while sexo != 'F' and sexo != 'M':
        sexo = str(input('╞Sexo [M/F]? ')).strip().upper()
        print('├──────────────────┐\n'
              '└──────────────────┘')
    if sexo == 'M':
        homem += 1
    if idade < 20 and sexo == 'F':
        mulherMenos20 += 1
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Mais uma pessoa [S/N]? ')).strip().upper()
    if continuar == 'N':
        break

print(f'{mais18} pessoas tem mais de dezoito anos\n'
      f'{homem} pessoas são homens\n'
      f'e {mulherMenos20} são mulheres com menos de 20 anos')

# fim
