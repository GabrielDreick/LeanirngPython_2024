'''
==================================================
Desenvolva um programa que leia o comprimento
de tres retas e diga ao usuario se elas podem
ou nao formar um triangulo.
==================================================
'''
########################################################################################################################
########################################################################################################################
########################################################################################################################
print('Me de 3 medidas e eu te direi se é possivel formar um triangulo com essa medidas.')
r1 = float(input('Pimeiro medida: '))
r2 = float(input('Segunda medida: '))
r3 = float(input('Terceira medida: '))

'''
if r1 > r2:
    a = r1
    b = r2
    
else:
    a = r2
    b = r1
    
if a < r3:
    c = a
    a = r3
    
else:
    c = r3



if a < b + c:
    print('É possivel formar um triangulo com essa medidas')
else:
    print(f'A medida {a} é grande demais para formar um triangulo com as medida {b} e {c}')
'''  # my code
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('É possivel formar um triangulo')
else:
    print('Essas medidas NÃO formam um triangulo')
