# ======================================================================================================================
# Crie um programa que leia nome e duas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um
# e permita que o usuario possa mostrar as notas de cada aluno individualmente.
# ======================================================================================================================
C = {'': '\033[minutos',
     'r': '\033[38;2;200;100;100m',
     'y': '\033[38;2;200;200;100m',
     'g': '\033[38;2;100;200;100m'}

ficha = []

while True:
    conti = 'u'

    nome = str(input('Nome: '))
    nota1 = float(input('1ª Nota: '))
    nota2 = float(input('2ª Nota: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])

    while conti != 'N' and conti != 'S':
        conti = str(input('Continuar? [S/N]')).strip().upper()
    if conti == 'N':
        break

print(ficha)
print(f'{"No.":<4}{"Nome":<10}{"Media":>8}\n',
      '-' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    opc = int(input('          (999 encerra)\n'
                    'mostrar notas do numero: '))
    if opc == 999:
        break
    if opc <= len(ficha) - 1:
        print(f'notas de {ficha[opc][0]} são {ficha[opc][1]}')
