print('\n'
      '\n'
      '==================================================\n'
      'Crie um programa que leia um número real qualquer\n'
      'pelo teclado e mostre na  tela a sua porção inteira.\n'
      'Ex:\n'
      'Digite um número: 6.127\n'
      'O número 6.127 tem a parte 6.\n'
      '==================================================\n'
      '')
######################################################################
######################################################################
from math import trunc

num = float(input('Digite um numero real: '))
print(f'Para o numero {num}, a sua parte inteira é {trunc(num)}.')
print(f'Para o numero {num}, a sua parte inteira é {num:.0f}.')
