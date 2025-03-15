tempo = int(input('Quantos anos tem seu carro? '))

if tempo <= 3:
    print('carro novo')
else:
    print('carro velho')
print('--FIM--\n')

print('carro novo' if tempo <= 3 else 'carro velho')  # de fato, meio confuso. prefiro os blocos "if, else"

print('''

''')
nome = input('Qual é o seu nome? ')
if nome == 'Gabriel':
    print('oh... ah...\n'
          f'O-Olá {nome}.')
else:
    print(f'Olá, prazer em te conhecer {nome}')
print('-----FIM-----')
if nome != 'Gabriel':
    print('hmm...\n')

n1 = float(input('Pimeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2
print(f'A sua media foi {m:.1f}')
if 5.9 < m < 8.0:
    print('A sua media foi boa, mas pode melhorar!')
if 8 < m < 10:
    print('A sua media foi otima!')
if m == 10:
    print('A sua media foi perfeita! Parabens')
elif m < 6:
    print('A sua media foi baixa, Estude Mais.')
