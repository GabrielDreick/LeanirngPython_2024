# ======================================================================================================================
# Faça um programa que leia 5 valores numericos e guarde-os em uma lista.
#
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista
# ======================================================================================================================
cor = {'': '\033[minutos',
       'i': '\033[38;2;255;0;255m',
       '^': '\033[38;2;255;255;0m',
       '^^': '\033[38;2;255;150;0m',
       'v': '\033[38;2;0;150;255m',
       'vv': '\033[38;2;0;0;255m'}
valores = []
print('Cinco numeros')
maior = menor = 0
for c in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]

print(f'Valores digitados: {valores}')
print(f'Maior valor: {maior}. Posição Tecnica: ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}. ', end='')
print()
print(f'Menor valor: {menor}. Posição Tecnica: ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}. ', end='')
print()

'''
maior = menor = valores[0]
for c in range(0, len(valores)):
    print(f'{cor["i"]}iteração: {c}{cor[""]}')
    print(f'Numero: {valores[c]}')
    print(f'{cor["^"]}maior: {maior}{cor[""]}')
    print(f'{cor["v"]}menor: {menor}{cor[""]}')
    if valores[c] > maior:
        maior = valores[c]
        print(f'{cor["^^"]}novo maior:', maior, '\033[0m')
    elif valores[c] < menor:
        menor = valores[c]
        print(f'{cor["vv"]}novo menor: {menor}{cor[""]}')
    print('=' * 30)
print(f'Maior numero: {maior}\n'
      f'Menor numero: {menor}')

for c in range(0, valores.count(maior)):
    posMaior.append(valores.index(maior, posMaior[c]))
print(posMaior)
'''  # (my) old non-functioning code

# fim
