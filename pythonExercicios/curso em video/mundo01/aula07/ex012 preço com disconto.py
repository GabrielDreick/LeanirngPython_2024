print('\n'
      '\n'
      '==================================================\n'
      'Faça um algoritimo que leia o preço de um produto\n'
      'e mostre seu novo preço com 5% de desconto.\n'
      '==================================================\n'
      '')

desconto = 5  # 5%

preco = float(input('Preço do produto: R$'))

preco2 = preco - ((desconto * preco) / 100)

print(f'Para um preço de R${preco}, um desconto de {desconto}% da um preço de R${preco2:.2f}')
