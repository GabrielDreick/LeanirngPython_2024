# ======================================================================================================================
# Crie um programa que tenha uma tupla unica com nomes de produtos e seus respectivos preços, na sequencia,
# No final, mostre uma listagem de preços, organizando os dado em forma tabular.
# ======================================================================================================================

produtos = ('Teclado', 172.89, 'Mouse', 139.99, 'Monitor', 116.89, 'Headphones', 158.89,
            'Caderno', 34.89, 'Lapis', 1.48, 'borracha', 1.10, 'Caneta', 2.29)

print('=' * 40)
for c in range(0, len(produtos), 2):
    print(f'{produtos[c]:_<16}R${produtos[c + 1]:.2f}')
print('=' * 40)

# fim
