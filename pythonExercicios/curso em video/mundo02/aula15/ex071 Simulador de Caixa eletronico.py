# ======================================================================================================================
# Crie um programa que simule o funcionamento de um caixa eletronico.
# no inicio, pergunte ao usuario qual será o valor a ser sacado (numero inteiro)
# e o programa vai informar quantas cedula de cada valor seão entregues.
#
# OBS: Considere que o caixa possui cedulas de R$50, R$20, R$10 e R$1.
# ======================================================================================================================
c = {'': '\033[0m',
     '50': '\033[38;2;230;210;80m',
     '20': '\033[38;2;220;220;100m',
     '10': '\033[38;2;220;150;120m',
     '1': '\033[38;2;150;220;150m',
     '#': '\033[38;2;100;100;100m'}
"""print(f'{c["50"]}Cinquenta{c[""]}\n'
      f'{c["20"]}Vinte{c[""]}\n'
      f'{c["10"]}Dez{c[""]}\n'
      f'{c["1"]}Um{c[""]}')
"""
print('='*30)
print(f'={"CAIXA ELETRONICO":^28}=')
print('='*30)
sacar = int(input('Valor a ser sacado: R$'))
print()
ceduCinquenta = ceduVinte = ceduDez = ceduUm = 0
while True:
    if sacar - 50 >= 0:
        sacar -= 50
        ceduCinquenta += 1
    elif sacar - 20 >= 0:
        sacar -= 20
        ceduVinte += 1
    elif sacar - 10 >= 0:
        sacar -= 10
        ceduDez += 1
    elif sacar - 1 >= 0:
        sacar -= 1
        ceduUm += 1
    elif sacar - 1 == -1:
        break
    else:
        print('...ãh?\n')
        break
print(f'{c["50"] if ceduCinquenta > 0 else c["#"]}{ceduCinquenta} Cedulas de Cinquenta Reais{c[""]}\n'
      f'{c["20"] if ceduVinte > 0 else c["#"]}{ceduVinte} Cedulas de Vinte Reais{c[""]}\n'
      f'{c["10"] if ceduDez > 0 else c["#"]}{ceduDez} Cedulas de Dez Reais{c[""]}\n'
      f'{c["1"] if ceduUm > 0 else c["#"]}{ceduUm} Cedulas de Um Real{c[""]}\n')

print('='*30)
if ceduCinquenta > 0:
    print(f'{c["50"]}{ceduCinquenta} Cedulas de Cinquenta Reais{c[""]}')
if ceduVinte > 0:
    print(f'{c["20"]}{ceduVinte} Cedulas de Vinte Reais{c[""]}')
if ceduDez > 0:
    print(f'{c["10"]}{ceduDez} Cedulas de Dez Reais{c[""]}')
if ceduUm > 0:
    print(f'{c["1"]}{ceduUm} Cedulas de Um Real{c[""]}')
print('='*30)

# fim
