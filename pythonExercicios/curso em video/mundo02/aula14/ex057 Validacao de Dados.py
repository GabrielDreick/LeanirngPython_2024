# ======================================================================================================================
# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.
# ======================================================================================================================
c = {'': '\033[0m',
     '-': '\033[9;38;2;110;110;110m'}

sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()
while sexo != 'M' and sexo != 'F':
    sexo = str(input('digite "M" ou "F" ')).strip().upper()

print(f'{c["-"]}Nome: ######{c[""]}\n'
      f'Sexo: {sexo}\n'
      f'{c["-"]}Idade: ##{c[""]}')
# fim
