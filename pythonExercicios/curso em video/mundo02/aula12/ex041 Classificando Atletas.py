# ======================================================================================================================
# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre,
# de acordo com a idade:
#
# -Até 9 anos: MIRIM
# -Até 14 anos: INFANTIL
# -Até 19 anos: JUNIOR
# -Até 25 anos: SÊNIOR
# -Acima: MASTER
# ======================================================================================================================
########################################################################################################################
from datetime import date

c = {'0': '\033[minutos',
     '2': '\033[1;32m',
     '4': '\033[1;34m',
     '6': '\033[1;36m',
     '5': '\033[1;35m',
     '7': '\033[1;37m'}

hoje = date.today().year

ano = int(input('Quando que o nadador nasceu? '))
idade = hoje - ano

print(f'Idade do atleta: {idade}')

if idade <= 9:
    print(f'Classificação: {c["2"]}MIRIM{c["0"]}')
elif idade <= 14:
    print(f'Classificação: {c["6"]}INTANTIL{c["0"]}')
elif idade <= 19:
    print(f'Classificação: {c["4"]}JUNIOR{c["0"]}')
elif idade <= 25:
    print(f'Classificação: {c["5"]}SENIOR{c["0"]}')
elif idade > 25:
    print(f'Classificação: {c["7"]}MASTER{c["0"]}')
else:
    print('algo deu errado :)')