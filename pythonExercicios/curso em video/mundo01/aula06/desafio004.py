print()
print('========================================')
print('Faça um programa que leia algo pelo')
print(' teclado e mostre na tela o seu tipo')
print(' primitivo e todas as informações')
print(' possives sobre ele.')
print('========================================')
print()

x = input('Digite algo: ')

print(x)
print(type(x))
print('Apenas espaço:', x.isspace())
print('Alfabetico:', x.isalpha())
print('Capitalizada:', x.istitle())
print('Apenas Maiuscula:', x.isupper())
print('Apenas Minuscula:', x.islower())
print('digito:', x.isdigit())
print('Alfanumerico:', x.isalnum())
print('numerico:', x.isnumeric())
print('decimal:', x.isdecimal())
print('Imprimivel:', x.isprintable())
print('ascii:', x.isascii())
print('-Identifier-:', x.isidentifier())
