'''
====================[Desafio033]====================
Faça um programa que leia tres numeros e mostre
qual e o maior e e qual e o menor.
====================================================
'''

########################################################################################################################
########################################################################################################################
########################################################################################################################

n1 = int(input('Pimeiro numero: '))
n2 = int(input('Segundo numero: '))
n3 = int(input('Terceiro numero: '))

if n1 == n2 == n3:
    print('sao todos iguais')

# se PRIMEIRO é maior que SEGUNDO, e assimilando posições
if n1 > n2:
    maior = n1
    medio = n2
else:
    maior = n2
    medio = n1

# se MAIOR é maior que TERCEIRO, e rearranjando posições
if maior > n3:
    menor = n3
else:
    menor = medio
    medio = maior
    maior = n3

if medio < menor:
    x = medio
    medio = menor
    menor = x

print(f'{maior} é o maior numero\n'
      f'{menor} é o menor numero')
