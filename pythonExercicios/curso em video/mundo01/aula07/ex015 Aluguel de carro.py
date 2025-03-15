print('\n'
      '\n'
      '==================================================\n'
      'Escreva um programa que pergunte a quantidade de\n'
      'Km percorridos por um carre alugado e a quantidade\n'
      'de dias pelos quais ele foi alugado. Calcule o\n'
      'preço a pagar, sabendo que o carro custa\n'
      'R$60 por dia e R$0.15 por Km rodado.\n'
      '==================================================\n'
      '')
######################################################################
######################################################################
diaria = 60
distancia = 0.15

dia = int(input('O carro foi alugado por quantos dias: '))
km = float(input('E percorreu quantos Kilometros: '))

preco = (diaria * dia) + (distancia * km)

print('\n'
      f'O total a pagar por {dia} dias e {km}Km é R${preco:.2f}')
