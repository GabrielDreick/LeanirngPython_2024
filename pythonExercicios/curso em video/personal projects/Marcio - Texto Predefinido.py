from datetime import datetime
print()

def down(size=30):
    print('\n' * size)


def real_input(txt=''):
    while True:
        try:
            n = float(str(input(txt)).replace(',', '.'))
        except TypeError:
            print('digite um numero real')
        else:
            return n


now = datetime.today().time().hour

timeofday = 'indefinido'
if now < 12:
    timeofday = 'Bom dia'
elif 12 <= now < 19:
    timeofday = 'Boa tarde'
elif 19 <= now < 24:
    timeofday = 'Boa noite'

name = str(input(f'Nome do cliente: ')).strip().title()
if not name == '':
    name = ', ' + name

intro = f"{timeofday}{name}."

after_intro = str(input('                           (ou deixar em branco)\n'
                        'voce pode escrever algo antes da lista aqui >'))


dict_titulos = {}
dict_plataforma = {}

for nTitulos in range(0, int(input('Quantos Titulos?'))):
    dict_plataforma.clear()
    titulo = "*" + str(input(f"Nome do {nTitulos+1}º titulo: ")).upper() + "*"
    for nItens in range(0, int(input(f"Quantos itens para \033[1;32m{titulo}\033[0m? "))):
        item = "- " + str(input(f"item {nItens+1}: ")) + ". R$"
        preco = real_input("R$")
        dict_plataforma[item] = preco
    dict_plataforma["Mao de obra: R$"] = real_input('Mao de obra: R$')

    dict_titulos[titulo] = dict_plataforma.copy()

mostrarsoma = str(input("mostrar a soma dos materias em cada titulo? [SIM/NAO] "))
if mostrarsoma.upper() in ['S', 'SIM']:
    mostrarsoma = True

print('\033[32m')
print(f"{intro}")
print(f"{after_intro}")

for keyTitulo, valueItens in dict_titulos.items():
    print()
    print(f"\033[1m{keyTitulo}\033[0;32m")
    for keySubtitulo, valueSubvalor in valueItens.items():
        print(f"{keySubtitulo}{valueSubvalor}")
    if mostrarsoma:
        soma = 0
        for c in valueItens.values():
            soma += c
        print(f'Materiais: R${soma}')
