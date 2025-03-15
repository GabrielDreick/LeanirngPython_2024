# ======================================================================================================================
# Crie um programa que leia vários números inteiros pelo teclado. no final da execução,
# mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuario se ele quer ou não continuar a digitar valores.
# ======================================================================================================================
continuar = 'S'
maior = menor = total = contador = 0
while continuar == 'S':
    num = int(input('Numero'))

    if contador == 0:
        maior = num
        menor = num

    if num > maior:
        maior = num
    elif num < menor:
        menor = num

    contador += 1
    total += num

    continuar = input('continuar? [S/N]').upper().strip()
    if continuar != 'S':
        continuar = 'N'

media = total / contador

print(f'A media de todos os {contador} numeros que você digitou da {media}\n'
      f'O maior numero foi {maior} e o menor numero foi {menor}')

# fim
