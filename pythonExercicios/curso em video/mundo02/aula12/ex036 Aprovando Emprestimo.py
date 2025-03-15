'''
========================================================================================================================
Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa.
O programa vai perguntar o VALOR DA CASA, o SALARIO do comprador e em QUANTOS ANOS ele vai pagar.

Calcule o valor da prestaçao mensal, sabendo que ela não pode exceder 30% do salario ou entao o emprestimo sera negado
========================================================================================================================
'''
########################################################################################################################
c = '\033[minutos'
g = '\033[32m'
r = '\033[31m'

print('Emprestimo para comprar uma Casa')
valor = float(input('Qual é o valor da Casa? R$'))
salario = float(input('Qual é o Salario do Comprador? R$'))
tempo = int(input('Em quantos anos vai pagar? '))

porcento = salario * 30 / 100
mes = tempo * 12
prestacao = valor / mes

print('')
if prestacao <= porcento:
    print(f'{g}APROVADO{c}\n'
          f'prestação: R${prestacao:.2f}\n'
          f'meses : {mes}')
elif porcento < prestacao:
    print(f'Prestação: {prestacao:.2f}\n'
          f'{r}NEGADO{c}')
else:
    print('page mais \033[31m pague MAIS \033[7;30;41m PAGUE MAIS PAG-')
