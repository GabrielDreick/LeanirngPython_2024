# ======================================================================================================================
# Crie um programa que leia o nome e o preço de vários produtos. O programa devera perguntar se o usuario vai continuar.
# No final, mostre:
#
# A) Qual é o total gasto na compra.
# B) Quantos produtos custam mais de R%1000.
# C) Qual é o nome do produto mais barato.
# ======================================================================================================================
c = {'': '\033[0m',
     'none': '\033[38;2;75;75;75m'}
k = c['none']
print('''
==============================
             LOJA             
==============================
''')
precoBarato = total = quantoK = quantosProdutos = 0
maisBarato = continuar = ''
while True:
    continuar = ''
    produto = str(input('Nome do produto: ')).strip().title()
    preco = float(input('Preço do produto: R$'))
    total += preco
    quantosProdutos += 1
    if quantosProdutos == 1 or preco < precoBarato:
        precoBarato = preco
        maisBarato = produto
    if preco > 1000:
        k = c['']
        quantoK += 1
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Passar outro produto [S/N]?')).strip().upper()
    if continuar == 'N':
        break
print(f'\n'
      f'\n'
      f'\n'
      f'Passou {quantosProdutos} produtos.\n'
      f'Total: R${total:.2f}\n'
      f'{k}{quantoK} produto(segundos) custa(m) mais de R$1000{c[""]}\n'
      f'O produto mais barato foi {maisBarato} custando R${precoBarato:.2f}')

# fim
