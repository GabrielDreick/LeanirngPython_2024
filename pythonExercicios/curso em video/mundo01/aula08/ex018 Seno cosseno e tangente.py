print('\n'
      '\n'
      '==================================================\n'
      'Faça um programa que leia um ângulo qualquer e\n'
      'mostre na tela o valor do seno, cosseno e tangente\n'
      'desse ângulo.\n'
      '==================================================\n'
      '')
######################################################################
######################################################################
from math import radians, sin, cos, tan

a = float(input('digite um angulo: º'))

sin = sin(radians(a))
cos = cos(radians(a))
tan = tan(radians(a))

print('\n'
      f'\n'
      f'O Angulo de {a} tem o Seno de {sin:.2f}\n'
      f'O Angulo de {a} tem o Cosseno de {cos:.2f}\n'
      f'O Angulo de {a} tem A Tangente de {tan:.2f}')
