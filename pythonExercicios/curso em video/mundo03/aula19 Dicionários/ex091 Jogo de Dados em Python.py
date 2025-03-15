# ======================================================================================================================
# Crie um programa onde 4 jogadore joguem um dado e tenham resultados aleatorios.
# Guarde esses resultados em um dicionario.
# No final, coloque esse dicionario em ordem, sabendo que o vencedor tirou o maior numero no dado.
# ======================================================================================================================
from random import randint

lista = []
x = maior = menor = 0
for c in range(0, 4):
    jogo = {'nome': f'jogador{c+1}', 'dado': randint(1, 6)}

    print(f'O {jogo["nome"]} rolou o dado e caiu {jogo["dado"]}')
    if c == 0:
        lista.append(jogo.copy())
        maior = menor = jogo['dado']
    elif jogo['dado'] <= menor:
        lista.append(jogo.copy())
    elif jogo['dado'] >= maior:
        lista.insert(0, jogo.copy())
        maior = jogo['dado']

print(lista)
x = 0
for c in range(0, len(lista)):
    print(f'{x + 1}° Lugar {lista[x]["nome"]} quem rolou {lista[x]["dado"]}')
    x += 1
