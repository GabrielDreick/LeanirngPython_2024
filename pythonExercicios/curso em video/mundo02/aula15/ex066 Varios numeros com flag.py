# ======================================================================================================================
# Crie um programa que leia varios numeros inteiros pelo teclado.
# O programa so vai parar quando o usuario digitar o valor 999, quê é a condiçao de parada.
# No final, mostre quantos numeros foram digitados e qual foi a soma entre eles
# (desconsiderando o flag).
# ======================================================================================================================
soma = total = 0
print('Você vai me dar numeros para eu somar, digite ´´´999```par parar.')
while True:
    n = int(input('Numero: '))
    if n == 999:
        break
    soma += n
    total += 1
print(f'A soma de todos os {total} numeros que voce digitou, dá {soma}')

# fim
