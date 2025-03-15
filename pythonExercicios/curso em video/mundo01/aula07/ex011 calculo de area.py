print('\n'
      '\n'
      '==================================================\n'
      'Faça um programa que leia a largura e a altura de\n'
      'uma parede em metros, calcule a sua area e a\n'
      'quantidade de tinta necessaria para pinta-la,\n'
      'sabendo que cada litro de tinta pinta uma\n'
      'area de 2M².\n'
      '\n'
      '==================================================\n'
      '')

print('Vou te dizer quanto de tinta você vai precisar para pintar uma parede,\n'
      'mas, para isso, vou precisar saber alguns valores.\n'
      '')
larg = float(input('Quantos metros de largura: '))
altu = float(input('Quantos metros de altura: '))
area = larg * altu
litro = area / 2

print(f'\n'
      f'{larg}M de largura e {altu}M de altura da uma area de {larg*altu}M²,\n'
      f'sera necessario {litro}L de tinta.')
