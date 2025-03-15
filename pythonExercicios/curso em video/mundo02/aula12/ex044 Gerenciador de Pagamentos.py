# ======================================================================================================================
# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando seu preço normal e condição de pagamento:
#
# -Á vista dinheiro/cheque: 10% de desconto
# -Á vista no cartão: 5% de desconto
# -Em até 2x no cartão: preço normal
# -3x ou mais no cartão: 20% de juros
# ======================================================================================================================
########################################################################################################################
c = {'': '\033[minutos',
     '1': '\033[31m',
     '2': '\033[32m',
     '3': '\033[33m',
     '4': '\033[34m',
     '5': '\033[35m',
     '6': '\033[36m',
     '7': '\033[37m'}  # cores

din = 10
car = 5
juros = 20

preco = float(input('Preço das compras: R$'))

dinheiro = preco - (preco * din / 100)
cartao = preco - (preco * car / 100)
duasvezes = preco
tresoumais = preco + (preco * juros / 100)

pagamento = int(input(f'[ 1 ] = {c["2"]}dinheiro{c[""]}\n'
                      f'[ 2 ] = {c["3"]}cartão{c[""]}\n'
                      'Qual sera a forma de pagamento? >'))
print()

if pagamento == 1:
    print(f'{c["2"]}Dinheiro{c[""]} a {c["2"]}vista{c[""]} recebe {c["2"]}{din}%{c[""]} de desconto:\n'
          f'{c["7"]}preço: R${preco:.2f}{c[""]}\n'
          f'Desconto: R${dinheiro:.2f}')
elif pagamento == 2:
    prestacao = int(input(f'{c["6"]}A VISTA {car}%{c[""]} de desconto\n'
                          f'{c["4"]}ATÉ 2 VEZES{c[""]} preço normal\n'
                          f'{c["1"]}3 VEZES OU MAIS {juros}%{c[""]} de {c["1"]}JUROS{c[""]}\n'
                          'Vai parcelar em quantas vezes? '))
    print('\n\n')

    if prestacao == 1:
        print(f'{c["3"]}Cartão{c[""]} a {c["6"]}vista{c[""]} recebe {c["6"]}{car}%{c[""]} de desconto:\n'
              f'{c["7"]}Preço: R${preco:.2f}{c[""]}\n'
              f'Descontado: R${cartao:.2f}')

    elif 1 < prestacao <= 2:
        print(f'{c["3"]}Cartão{c[""]} parcelado até {c["4"]}duas vezes{c[""]}:\n'
              f'Preço: {preco:.2f}\n'
              f'Prestação: R${duasvezes / prestacao}')

    elif prestacao > 2:
        print(f'{c["3"]}Cartão{c[""]} parcelando {c["5"]}{prestacao} vezes{c[""]} recebe '
              f'{c["1"]}{juros}%{c[""]} de {c["1"]}juros{c[""]}:\n'
              f'{c["7"]}Preço: R${preco:.2f}{c[""]}\n'
              f'Com Juros: R${tresoumais:.2f}\n'
              f'Prestação: R${tresoumais / prestacao:.2f}')
    else:
        print(f'não acho que de pra pagar assim, {c["1"]}vou ter que te expulsar{c[""]}')
else:
    print(f'não entendi, {c["7"]}vou embora{c[""]}')
