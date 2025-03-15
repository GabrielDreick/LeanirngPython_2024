print('''

      ==================================================
      Crie um programa que leia o nome de uma pessoa
      e diga se ela tem "SILVA" no nome.
      ==================================================
      ''')
######################################################################
######################################################################
nome = str(input('Nome completo: ')).strip()
n = 'SILVA' in nome.upper()
print(f'Esse nome contem "SILVA": {n}')
