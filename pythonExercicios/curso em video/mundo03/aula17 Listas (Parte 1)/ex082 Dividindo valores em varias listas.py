# ======================================================================================================================
# Crie um programa que vai ler varios numeros e colocar em uma lista.
# Depois disso, crie duas listas extras que vao conter apenas os valores pares e os valores impares digitados,
# respectivamente.
# Ao final, mostre o conteudo das tres listas geradas.
# ======================================================================================================================
numeros = []
pares = []
impares = []
print('Adicione numeros')
while True:
    conti = ''
    numeros.append(int(input('Numero: ')))
    while conti != 'S' and conti != 'N':
        conti = str(input('Continuar? [S/N] ')).strip().upper()
    if conti == 'N':
        break

for separando in numeros:
    if separando % 2 == 0:
        pares.append(separando)
    elif separando % 2 != 0:
        impares.append(separando)

print(f'  Todos: {numeros}')
print(f'  Pares: {pares}')
print(f'Impares: {impares}')

for limpando in range(0, len(numeros)):         # limpando
    numeros.pop()
print(numeros)

# fim
