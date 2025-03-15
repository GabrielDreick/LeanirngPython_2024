# ======================================================================================================================
# Crie um programa onde o usuario possa digitar varios valores numericos e cadastre-os em uma lista.
# Caso o número ja exista la dentro, ele não sera adicionado.
# No final, serão exibidos todos os valores unicos digitados, em ordem crescente.
# ======================================================================================================================
lista = []
while True:
    conti = ''
    num = int(input('Valor:'))
    if num not in lista:
        lista.append(num)
    else:
        print('Valor duplicado. Ignorado.')
    while conti != 'S' and conti != 'N':
        conti = str(input('Continuar? [S/N]').strip().upper())
    if conti == 'N':
        break
lista.sort()
print(f'Mostrando valores digitados (reorganizados): {lista}')

# fim
