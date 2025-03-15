# ======================================================================================================================
# Crie um programa que leia nome e duas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um
# e permita que o usuario possa mostrar as notas de cada aluno individualmente.
# ======================================================================================================================
C = {'': '\033[minutos',
     'r': '\033[38;2;200;100;100m',
     'y': '\033[38;2;200;200;100m',
     'g': '\033[38;2;100;200;100m'}

listaGeral = []
dados = []
while True:
    conti = ''

    print('\n' * 30)
    dados.insert(0, str(input('NOME: ')).capitalize())
    dados.insert(1, float(input('1ª NOTA: ')))
    dados.insert(2, float(input('2ª NOTA: ')))
    dados.insert(3, (dados[1] + dados[2]) / 2)
    listaGeral.append(dados[:])
    dados.clear()

    while conti != 'S' and conti != 'N':
        conti = str(input('Continuar? [S/N]')).strip().upper()
    if conti == 'N':
        break

print('\n' * 10)

while True:
    acao = int(input('[2] Mostrar Medias\n'
                     '[1] Mostrar Notas\n'
                     '[0] sair\n'
                     '>'))
    print('\n' * 5)

    if acao == 0:
        break

    elif acao == 1:
        for c in range(0, len(listaGeral)):
            print(f'=' * 30 + '\n'
                  f'Nome: {listaGeral[c][0]}\n'
                  f'Notas: {listaGeral[c][1:3]}\n' +
                  f'=' * 30 + '\n' * 2)

    elif acao == 2:
        for c in range(0, len(listaGeral)):
            media = listaGeral[c][3]
            if media > 7:
                cor = 'g'
            elif 5 <= media < 7:
                cor = 'y'
            elif media < 5:
                cor = 'r'
            print(f'=' * 30 + '\n'
                  f'Nome: {listaGeral[c][0]}\n'
                  f'Media: {C[cor]}{listaGeral[c][3]:.1f}{C[""]}\n' +
                  f'=' * 30 + '\n' * 2)

# fim
