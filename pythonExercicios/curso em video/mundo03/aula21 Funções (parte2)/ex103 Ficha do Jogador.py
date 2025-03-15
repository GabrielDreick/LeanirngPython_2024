# ======================================================================================================================
# Faça um programa que tenha uma fanção chamada ficha(), que receba dois parametros opcional:
# o nome de um jogador e quantos gols ele marcou.
#
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado.
# ======================================================================================================================
def ficha(name='[nome não informado]', goals=000):
    print(f'O Jogador {name} fez {goals} gol(s)')


# ╔════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║                                                    MAIN PROGRAM                                                    ║
# ╚════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝

nome = str(input('Nome do Jogador: '))
gol = str(input('Gols marcados: '))
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 000
if nome.strip() == '':
    ficha(goals=gol)
else:
    ficha(nome, goals=gol)

# fim
