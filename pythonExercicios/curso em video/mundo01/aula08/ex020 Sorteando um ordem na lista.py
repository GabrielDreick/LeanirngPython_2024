print('\n'
      '\n'
      '==================================================\n'
      'O mesmo professo do desafio anterior quer sortear\n'
      'a ordem de apresentação de trabalhos do alunos.\n'
      'Faça um programa que leia o nome dos quatro alunos\n'
      'e mostre a ordem sorteada.\n'
      '==================================================\n'
      '')
######################################################################
######################################################################
from random import shuffle

n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')

lista = [n1, n2, n3, n4]
shuffle(lista)

print(f'A ordem de apresentação é:\n'
      f'{lista}')
