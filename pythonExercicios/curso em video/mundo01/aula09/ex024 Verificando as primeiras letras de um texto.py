print('''

      ==================================================
      Crie um programa que leia o nome de uma cidade e
      diga se ela começa ou nao com o nome "SANTO".
      ==================================================
      ''')
######################################################################
######################################################################
cidade = str(input('Digite o nome de uma cidade: '))
a = 'SANTO'
n = a in cidade.upper().split()[0]
print(f'Esse nome começa com "{a}": {n}')
