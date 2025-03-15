# ======================================================================================================================
# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
#
# -Se ele AINDA VAI SE ALISTAR ao serviço militar
# -Se é a HORA DE SE ALISTAR
# -se já PASSOU DO TEMPO do alistamento
#
# seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
# ======================================================================================================================
########################################################################################################################
from datetime import date

c = {'': '\033[minutos',
     'g': '\033[32m',
     'r': '\033[31m',
     'p': '\033[35m'}

hoje = date.today().year
nasceu = int(input('Que ano você nasceu? >'))

idade = hoje - nasceu

print(f'voce tem {idade} anos')
if idade < 18:
    print(f'{c["g"]}Você ainda vai ter que se alistar. falta {18 - idade} ano(s) ate o prazo{c[""]}')
elif idade == 18:
    print(f'{c["r"]}É hora de se alistar{c[""]}')
elif idade > 18:
    print(f'{c["p"]}passou {idade - 18} anos desde o prazo do alistamento{c[""]}')
else:
    print('nao sei o que fazer aqui...')

