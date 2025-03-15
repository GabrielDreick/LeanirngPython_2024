print('\n'
      '\n'
      '==================================================\n'
      'Faca um programa do cateto oposto e do cateto\n'
      'adjacente de um triângulo retângulo, calcule\n'
      'e mostre o comprimento da hipotenusa.\n'
      '==================================================\n'
      '')
######################################################################
######################################################################
from math import sqrt, hypot

co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjacente: '))
# horas = sqrt(co ** 2 + ca ** 2)
h = hypot(co, ca)

print(f'a hipotenusa é {h:.2f}')
