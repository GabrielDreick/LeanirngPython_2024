# ======================================================================================================================
# Crie um programa que vai ler varios numeros e colocar em uma lista.
# Depois disso, mostre:
#
# A) Quantos numeros foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.
# ======================================================================================================================
lista = []
while True:
    conti = ''
    lista.append(int(input('Numero: ')))
    while conti != 'S' and conti != 'N':
        conti = str(input('Continuar? [S/N] ')).strip().upper()
    if conti == 'N':
        break
lista.sort(reverse=True)
print(f'\n{len(lista)} valores digitados')
print(f'Ordem decrescente: {lista}')
if 5 in lista:
    print('Existe o valor [5] na lista')
else:
    print('Não existe o valor [5] na lista')

# fim
