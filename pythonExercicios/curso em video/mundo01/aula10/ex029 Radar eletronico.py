'''
====================[Desafio029]====================
Escreva um programa que leia a velocidade de um
carro.

Se ele ultrapassar 80Km/horas, mostre uma mensagem
dizendo que ele foi multado.

A multa vai custar R$7,00 por cada Km acima
do limite.
====================================================
'''
########################################################################################################################
########################################################################################################################
########################################################################################################################
limite = 80
multa = 7.00
velo = float(input('velocidade: Km '))
print()

if velo > limite:
    multado = (velo - limite) * multa
    print('LIMITE EXCEDIDO\n'
          f'Velocidade: {velo}Km/horas\n'
          f'Multa : R${multado:.2f}')
else:
    print(f'dentro do limite\n'
          f'Velocidade: {velo}Km/horas')
