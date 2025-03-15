# ======================================================================================================================
# Faça um pragrama que leia nome e peso de varias pessoa, guardando tudo em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.
# ======================================================================================================================

pessoas = []
pesos = [[], []]
dados = []
menor = maior = 0
while True:
    conti = ''
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    elif dados[1] > maior:
        maior = dados[1]
    elif dados[1] < menor:
        menor = dados[1]

    pessoas.append(dados[:])
    dados.clear()

    while conti != 'S' and conti != 'N':
        conti = str(input('Continuar? [S/N] >')).strip().upper()
    if conti == 'N':
        break

for p in pessoas:
    if p[1] == maior:
        pesos[0].append(p[0])
    elif p[1] == menor:
        pesos[1].append(p[0])

print(f'{len(pessoas)} Pessoas Cadastradas.')
print(f'{maior}Kg é o peso mais pesado e é o peso de: {pesos[0]}')
print(f'{menor}Kg é o peso mais leve e é o peso de: {pesos[1]}')

# fim
