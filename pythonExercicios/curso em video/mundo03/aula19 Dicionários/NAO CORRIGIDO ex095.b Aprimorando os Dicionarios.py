# ======================================================================================================================
# Aprimore o Desafio 093 para que ele funcione com varios jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
# ======================================================================================================================

dados = {}
listaGols = []
listaJogadores = []

print('\n' * 30)
print("=" * 30)
print(f"{'Aproveitamento':^30}\n"
      f"{'Jogadores de Futebol':^30}")
print("=" * 30)

while True:
    listaGols.clear()

    dados["nome"] = str(input('Nome do Jogador: ')).strip().title()
    dados["quantasPartidas"] = int(input('Partidas Jogadas: '))

    for c in range(0, dados["quantasPartidas"]):
        gols = int(input(f'Quantos gols na {c+1}ª partida? >'))
        listaGols.append(gols)
    dados["listaGols"] = listaGols.copy()
    dados["totalGols"] = sum(listaGols)

    listaJogadores.append(dados.copy())
    dados.clear()

    conti = ''
    while conti != "S" and conti != "N":
        conti = str(input("Continuar? [S/N]")).strip().upper()
    if conti == "N":
        break

print('-' * 40)
for k, v in enumerate(listaJogadores):
    print(f'{k:>3}', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
'''
print('\n' * 30)
print(listaJogadores)
for jogador in listaJogadores:
    print('=' * 30)
    print(f'Jogador {jogador["nome"]} jogou {jogador["quantasPartidas"]} partidas')
    for i, gol in enumerate(jogador['listaGols']):
        print(f'    Na partida {i+1}, Marcou {gol}')
    print(f'O total de Gols foi {jogador["totalGols"]}')
    print()
'''