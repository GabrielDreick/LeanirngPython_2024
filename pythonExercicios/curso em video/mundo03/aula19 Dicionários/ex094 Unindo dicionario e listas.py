# ======================================================================================================================
# Crie um programa que leia nome, sexo e idade de varias pessoas,
# guardando os dados de cada pessoa em um dicionario e todos os dicionarios em uma lista.
# No final, mostre:
# A) Quantas pessoa foram cadastradas.
# B) A média de idade do grupo.
# C) Uma lista com todas as mulheres.
# D) Uma lista com todas as pessoas com idade acima da média.
# ======================================================================================================================
dados = {}
listaGeral = []
listaMulheres = []
listaAcimaMedia = []
contador = media = 0

while True:
    dados.clear()
    contador += 1
    dados["nome"] = str(input('Nome: ')).strip().title()

    dados["sexo"] = ''
    while dados["sexo"] != 'M' and dados['sexo'] != 'F':
        dados["sexo"] = str(input('Sexo: [M/F] >')).strip().upper()

    dados["idade"] = int(input('Idade: '))
    while dados["idade"] < 0:
        print(f'espera que eu acredite que {dados["nome"]} tem {dados["idade"]} anos?')
        dados["idade"] = int(input('Idade: '))

    listaGeral.append(dados.copy())
    media += dados['idade']

    if dados['sexo'] == 'F':
        listaMulheres.append(dados.copy())

    conti = ''
    while conti != 'S' and conti != 'N':
        conti = str(input('\n    Continuar? [S/N]')).strip().upper()
    if conti == 'N':
        break


media = media / len(listaGeral)

for c in listaGeral:
    if c['idade'] > media:
        listaAcimaMedia.append(c.copy())

print('\n' * 20)
print('Lista Geral')
print('=' * 20)
for c in listaGeral:
    print(f'Nome: {c["nome"]}\n'
          f'Sexo: {c["sexo"]}\n'
          f'Idade: {c["idade"]}\n')
print('=' * 20)

print('\n' * 2)
print('Lista de Mulheres')
print('=' * 20)
for c in listaMulheres:
    print(f'Nome: {c["nome"]}\n'
          f'Idade: {c["idade"]}\n')
print('=' * 20)

print('\n' * 2)
print(f'Lista de pessoas com idade acima da media, que é {media} anos')
print('=' * 20)
for c in listaAcimaMedia:
    print(f'Nome: {c["nome"]}\n'
          f'Sexo: {c["sexo"]}\n'
          f'Idade: {c["idade"]}\n')
print('=' * 20)

# fim
