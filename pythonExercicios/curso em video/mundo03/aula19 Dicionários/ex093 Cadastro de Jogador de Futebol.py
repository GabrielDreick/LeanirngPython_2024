# ======================================================================================================================
# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso sera guardado num dicionário, incluindo o total de gols feitos durante o campeonato.
# ======================================================================================================================
totalGols = 0
listaGols = []
dados = {}

print('\n' * 30)
print("=" * 30)
print(f"{'Aproveitamento':^30}\n"
      f"{'Jogador de Futebol':^30}")
print("=" * 30)


dados["nome"] = str(input('Nome do Jogador: ')).strip().title()
dados["quantasPartidas"] = int(input('Partidas Jogadas: '))
for c in range(0, dados["quantasPartidas"]):
    listaGols.append(int(input(f'Quantos gols na {c+1}ª partida? >')))
    totalGols += listaGols[c]
dados["listaGols"] = listaGols
dados["totalGols"] = totalGols

print('\n' * 30)
print('=' * 30)
print(dados)

print('=' * 30)
for k, v in dados.items():
    print(f'a chave {k} tem o valor {v}')
print('=' * 30)

print(f'Jogador {dados["nome"]} jogou {dados["quantasPartidas"]} partidas')
for c in range(0, dados["quantasPartidas"]):
    print(f'    Na partida {c+1}, Marcou {dados["listaGols"][c]}')
print(f'O total de Gols foi {dados["totalGols"]}')

# fim
