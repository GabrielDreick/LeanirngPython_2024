print('\n'
      '\n'
      '==================================================\n'
      'Um professor quer sortear um do seus quatro alunos\n'
      'para apagar o quadro. Faça um programa que ajude\n'
      'ele, lendo o nome deles e escrevendo o nome do\n'
      'escolhido.\n'
      '==================================================\n'
      '')
######################################################################
######################################################################
from random import choice

a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')

lista = [a1, a2, a3, a4]

choice = choice(lista)
print('\n'
      f'Quem foi escolhido foi :{choice}')
