print('\n'
      '\n'
      '==================================================\n'
      'Crie um algoritmo que leia um número e mostre o seu\n'
      'dobro, triplo e raiz quadrada\n'
      '==================================================\n'
      '')

n = float(input('Me de um número: '))
nd = n * 2
nt = n * 3
nr = n ** .5

print(f'Para o numero {n}\n'
      f'o dobro é {nd}\n'
      f'o triplo é {nt}\n'
      f'e a raiz quadrada é {nr:.5f}')
