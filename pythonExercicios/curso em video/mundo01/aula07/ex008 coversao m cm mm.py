print('\n'
      '\n'
      '==================================================\n'
      'Escreva um programa que leia um valor em metros e\n'
      'o exiba convertidos em centimetros e milimetros\n'
      '==================================================\n'
      '')

print('Vou converter metros em cetimetro e milimetros')
m = float(input('Me de um numero de metros:'))

km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000

print(f'{m} Metro(s) é o mesmo que:\n'
      f'{km:.3f} Kilometros\n'
      f'{hm:.2f} Hequitometros\n'
      f'{dam:.2f} Decametros\n'
      f'{dm:.2f} Decimetros\n'
      f'{cm:.2f} Centimetros\n'
      f'{mm:.2f} Milimetros')
