'''
====================[Desafio034]====================
Escreva um programa que pergunte o salario de um
funcinario e calcule o valor do seu aumento.

para salarios superiores a R$1.250,00
calcule um aumento de 10%.

Para os inferiores ou iguais, o aumento é de 15%.
====================================================
'''
########################################################################################################################
########################################################################################################################
########################################################################################################################
limite = 1250
alto = 10
baixo = 15
salario = int(input('Qual é o salario? R$'))

x = baixo
if salario > limite:
    x = alto
# else:
#     x = baixo
aumento = salario + (salario * x / 100)

print(f'O salario de R${salario:.2f} com um aumento de {x}% resultando em R${aumento:.2f}')
