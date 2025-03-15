# ======================================================================================================================
# Refaça o DESAFIO009, mostrando a TABUADA de um numero que o usuario escolher, so que agora utilizando um LAÇO FOR.
# ======================================================================================================================

print('''
===== Faz Tabuada =====
''')
n = int(input('Tabuada para o numero: '))
vezes = int(input('Até quantas vezes: '))  # não foi pedido, mas fiz

for tabuada in range(1, vezes+1):
    print(f'{n} x {tabuada:2} = {n * tabuada}')

# fim
