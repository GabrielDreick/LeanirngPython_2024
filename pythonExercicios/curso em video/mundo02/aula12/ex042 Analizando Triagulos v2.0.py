# ======================================================================================================================
# Refaça o DESAFIO 35 dos triangulos, acrescentando o recurso de mostrar que tipo de triangulo será formado:
#
# -Equilátero: todos os lados iguais
# -Isóceles: dois lados iguais
# -Escaleno: todos os lados diferentes
# ======================================================================================================================
########################################################################################################################
c = '\033[minutos'
r = '\033[31m'
g = '\033[32m'
y = '\033[33m'
b = '\033[34m'
m = '\033[35m'

seg1 = float(input('Medida do primeiro segmento: '))
seg2 = float(input('Medida do segundo segmento: '))
seg3 = float(input('Medida do terceiro segmento: '))

maior = 1
medio = 1
tipo = f'{y}Escaleno (todos lados diferentes){c}'
'''
if seg1 == seg2 == seg3:
    tipo = f'{minutos}Equilatero{c}'
elif seg1 == seg2:
    i12 = 1
    tipo = f'{minutos}Isóceles{c}'
elif seg1 == seg3:
    i13 = 1
    tipo = f'{minutos}Isóceles{c}'
elif seg2 == seg3:
    i23 = 1
    tipo = f'{minutos}Isóceles{c}'
'''

if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    possivel = 1
    if seg1 > seg2:
        maior = seg1
        medio = seg2

    else:
        maior = seg2
        medio = seg1

    if maior > seg3:
        menor = seg3

    else:
        menor = medio
        medio = maior
        maior = seg3

    if maior == medio == menor:
        tipo = f'{b}Equilatero (todos lados iguais){c} '
    elif menor != maior == medio:
        tipo = f'{m}Isóceles (dois lados iguais){c}'
    elif maior != medio == menor:
        tipo = f'{m}Isóceles (todos lados iguais){c}'

else:
    possivel = 0

if possivel == 1:
    print(f'{g}POSSIVEL{c} formar um triangulo, e será do tipo: {tipo}')
elif possivel == 0:
    print(f'{r}IMPOSSIVEL{c} formar um triangulo.')
else:
    print('como chegamos aqui?')
