dados = list()
dados.append('Pedro')
dados.append(25)
print(dados[0])
print(dados[1])

# pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]]
# ┌────────────┬────────────┬───────────┐
# │┌──────────┐│┌──────────┐│┌─────────┐│
# ││'Pedro',25│││'Maria',19│││'João',32││
# │├───┬──┬───┤│├───┬──┬───┤│├───┬─┬───┤│
# ││ 0 │  │ 1 │││ 0 │  │ 1 │││ 0 │ │ 1 ││
# │└───┘  └───┘│└───┘  └───┘│└───┘ └───┘│
# ├───┬────────┼───┬────────┼───┬───────┘
# │ 0 │        │ 1 │        │ 2 │
# └───┘        └───┘        └───┘

pessoas = list()
pessoas.append(dados[:])

pessoas.append(['Maria', 19])
pessoas.append(['João', 32])
print(pessoas[1][1])
print(pessoas)
for p in pessoas:
    print(p[0])

galera = []
dado = []
for c in range(0, 5):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

print(galera)

totmaior = totmenor = 0
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmaior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmenor += 1

print(f'{totmaior} sao maiores de idade\n'
      f'{totmenor} sao menores de idade')
