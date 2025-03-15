print('''

==================================================
Crie um programa que leia o nome completo de um
pessoa e mostre:

-O nome com todas as letras maiusculas
-O nome com todas minusculas
-Quantas letras ao todo (sem considerar espaços)
-Quantas letras tem o primeiro nome
==================================================
''')
######################################################################
######################################################################
nome = str(input('Nome completo:')).strip()
print(f'''
Nome em Maisuculo: {nome.upper()}
Nome em Minusculo: {nome.lower()}
Quantas letras: {len(nome) - nome.count(' ')}
O primeiro nome é {nome.split()[0]} e tem {len(nome.split()[0])} letras
''')

# Quantas letras: {len(nome.replace(' ', ''))}
