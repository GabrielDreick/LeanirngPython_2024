print('\n'
      '\n'
      '==================================================\n'
      'Crie um programa que leia quanto dinheiro uma\n'
      'pessoa tem na carteira e mostre quantos dolares\n'
      'ela pode comprar.\n'
      ''
      'Considere\n'
      '(2024) US$1,00 = R$4,97\n'
      '==================================================\n'
      '')
dolar = 4.97

real = float(input('Vou te dizer quantos Dolares você pode comprar.\n'
                   'Quantos Reais você tem? :'))

r = real / dolar

print(f'Com R${real:.2f}, você pode comprar US${r:.2f}')
