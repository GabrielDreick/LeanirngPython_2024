# ======================================================================================================================
# Faça um programa que tenha um função chamada encreva(),
# que receba um texto qualquer com parametro e mostre uma mensagem com tamanho adaptavel.

# Ex:
# escreva('Olá, Mundo!')
#
# Saida:
# ~~~~~~~~~~~~~
#  Olá, Mundo!
# ~~~~~~~~~~~~~
# ======================================================================================================================
def excreva(txt):
    print('~' * (len(txt) + 2))
    print(f' {txt} ')
    print('~' * (len(txt) + 2))


excreva(str(input('digite algo: ')))
print('\n')
excreva(str(input('agora, escreva outra coisa: ')))

# fim
