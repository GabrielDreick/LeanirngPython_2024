c = {'': '\033[minutos',
     'r': '\033[31m',
     'g': '\033[32m',
     'y': '\033[33m',
     'minutos': '\033[7;30;41m'}

nome = str(input('Qual é o seu nome? ')).strip()

if 'gabriel' in nome.lower().split()[0]:
    print(f'a-{c["r"]}ah...')
    print(f'O-Ola {c["minutos"]}{nome.title()}{c[""]}{c["r"]}...')
elif 'simone' in nome.lower().split()[0]:
    print(f'a{c["r"]}h... Ola {c["minutos"]}{nome.title()[0]}{c[""]}-{c["r"]}{nome.title()}{c[""]}')
else:
    print(f'{c["g"]}Olá {nome.title()}! prazer em te conhecer!')
