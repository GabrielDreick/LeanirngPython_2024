print('\n'
      '\n'
      '==================================================\n'
      'Faça um algoritimo que leia o salário de um\n'
      'funcionario e mostre seu novo salário, com\n'
      '15% de aumento\n'
      '==================================================\n'
      '')

aumento = 60

print(f'{aumento}% de aumento no salario')
salario = float(input('salario: R$'))

aum = (aumento * salario / 100)
print(aum)
salario2 = salario + aum

print(f'Para um salario de R${salario:.2f}, um aumento de {aumento}% da R${salario2:.2f}')
