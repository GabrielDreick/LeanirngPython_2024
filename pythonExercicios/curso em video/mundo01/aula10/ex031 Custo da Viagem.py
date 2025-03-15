'''
==================================================
Desenvolva um programa que pergunte a distancia
de uma viagem em Km.
Calcule o preço da passagem, cobrando
R$0,50 por Km para viagens de ate 200Km
e R$0,45 para viagens mais longas.
==================================================
'''
########################################################################################################################
########################################################################################################################
limiar = 200
curto = 0.50
longo = 0.45
distancia = float(input(f'Tabela de Preços:\n'
                        f'Até {limiar}Km: R${curto:.2f} por Km\n'
                        f'Acima de {limiar}Km: R${longo:.2f} por Km\n'
                        f'A viagem vai ter quantos Kilometros? '))
if distancia <= limiar:
    preco = curto * distancia
else:
    preco = longo * distancia
print(f'O preço da viagem é R${preco:.2f} ')
