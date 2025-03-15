# ======================================================================================================================
# desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status,
# de acordo com a tabela abaixo:
#
# -Abaixo de 18.5: Abaixo do peso
# -Entre 18.5 e 25: Peso ideal
# -25 Até 30: Sobrepeso
# -30 até 40: Obesidade
# -Acima de 40: Obesidade mórbida
# ======================================================================================================================
########################################################################################################################
c = {'': '\033[minutos',
     'p': '\033[35m',
     't': '\033[36m',
     'y': '\033[33m',
     'r': '\033[31m',
     'M': '\033[7;30;41m'}

peso = float(input('Quanto você pesa? Kg'))
altura = float(input('Qual é a sua altura em metros? M'))

IMC = peso / (altura ** 2)

if IMC < 18.5:
    print(f'Indice de Massa Corporal: [{c["p"]}{IMC:.1f}<{c[""]}----{c["t"]}18.5{c[""]}]\n'
          f'Classe: {c["p"]}ABAIXO DO PESO{c[""]}')
elif 18.5 <= IMC < 25:
    print(f'Indice de Massa Corporal: [{c["p"]}18.5{c[""]}--{c["t"]}>{IMC:.1f}<{c[""]}--{c["t"]}25{c[""]}]\n'
          f'Classe: {c["t"]}PESO IDEAL{c[""]}')
elif 25 <= IMC < 30:
    print(f'Indice de Massa Corporal: [{c["t"]}25{c[""]}--{c["y"]}>{IMC:.1f}<{c[""]}--{c["y"]}30{c[""]}]\n'
          f'Classe: {c["y"]}SOBREPESO{c[""]}')
elif 30 <= IMC < 40:
    print(f'Indice de Massa Corporal: [{c["y"]}30{c[""]}--{c["r"]}>{IMC:.1f}<{c[""]}--{c["r"]}40{c[""]}]\n'
          f'Classe: {c["r"]}OBESIDADE{c[""]}')
elif 40 <= IMC:
    print(f'Indice de Massa Corporal: [{c["r"]}40{c[""]}----{c["M"]}>{IMC:.1f}{c[""]}]\n'
          f'Classe: {c["M"]}OBESIDADE MORBIDA{c[""]}')
else:
    print('\033[37m...wweeeeEEEEEeeeeee...')
