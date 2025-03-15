# ======================================================================================================================
# Crie um programa onde o usuário possa digitar cinco valores numericos e cadastre-os em uma lista,
# ja na posição correta de inserção (sem usar o sort()).
# No final, mostre a lista ordenada ta tela.
# ======================================================================================================================
print('5 numeros')

lista = []
for c in range(0, 5):
    num = int(input('Numero: '))
    if c == 0 or num > lista[-1]:
        lista.append(num)
        print('Adicionado; posição final')
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                print(f'Adicionado; posição {pos}')
                break
            pos += 1

print(lista)

# fim
