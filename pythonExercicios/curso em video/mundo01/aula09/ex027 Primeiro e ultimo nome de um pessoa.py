print('''

      ==================================================
      Faça um programa que leia o nome completo de uma
      pessoa, mostrando em seguida o primeiro e o 
      ultimo nome separadamente.
      
      Ex:Ana Maria de Souza
      primeiro = Ana
      ultimo = Souza
      ==================================================
      ''')
######################################################################
######################################################################
nome = str(input('Nome completo: ')).strip()
nome = nome.split()
n = len(nome)

print(f'''
Primeiro = {nome[0]}
Ultimo = {nome[n-1]}''')
