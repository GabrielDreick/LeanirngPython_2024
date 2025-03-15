c = '\033[minutos'
g = '\033[32m'
G = '\033[42m'
r = '\033[1;31m'
R = '\033[41m'
modo = bool(input('"'))

emprestimo = float(input('Valor do emprestimo: R$'))
salario = float(input('Salario: R$'))

porcento = salario * 30 / 100
prestacao = emprestimo / porcento

if not modo:
    if porcento > emprestimo / (5 * 12):
        print(f'{G} {c}{g}Aprovado para cinco (5) anos{G} {c}')
        preco = emprestimo / (5 * 12)
    elif porcento > emprestimo / (6 * 12):
        print(f'{G} {c}{g}Aprovado para seis (6) anos{G} {c}')
        preco = emprestimo / (6 * 12)
    elif porcento > emprestimo / (7 * 12):
        print(f'{G} {c}{g}Aprovado para sete (7) Anos{G} {c}')
        preco = emprestimo / (7 * 12)
    elif porcento > emprestimo / (8 * 12):
        print(f'{G} {c}{g}Aprovado para oito (8) anos{G} {c}')
        preco = emprestimo / (8 * 12)
    elif porcento > emprestimo / (9 * 12):
        print(f'{G} {c}{g}Aprovado para nove (9) anos{G} {c}')
        preco = emprestimo / (9 * 12)
    elif porcento > emprestimo / (10 * 12):
        print(f'{G} {c}{g}Aprovado para dez (10) anos{G} {c}')
        preco = emprestimo / (10 * 12)
    else:
        print(f'{R} {c}{r}NÃO foi Aprovado{R} {c}')
        preco = 0
    print(f'30% de {salario} = {porcento}\n',
          f'emprestimo / porcento = {prestacao:.1f} meses\n')

    if preco:
        print(f'prestaçao = {preco:.2f}')
else:
    if porcento > emprestimo / (5 * 12):
        print(f'{G} {c}{g}Aprovado para cinco (5) anos{G} {c}')
    if porcento > emprestimo / (6 * 12):
        print(f'{G} {c}{g}Aprovado para seis (6) anos{G} {c}')
    if porcento > emprestimo / (7 * 12):
        print(f'{G} {c}{g}Aprovado para sete (7) anos{G} {c}')
    if porcento > emprestimo / (8 * 12):
        print(f'{G} {c}{g}Aprovado para oito (8) anos{G} {c}')
    if porcento > emprestimo / (9 * 12):
        print(f'{G} {c}{g}Aprovado para nove (9) anos{G} {c}')
    if porcento > emprestimo / (10 * 12):
        print(f'{G} {c}{g}Aprovado para dez (10) anos{G} {c}')
    else:
        print(f'{R} {c}{r}NÃO foi aprovado{R} {c}\n')
    print(f'30% de {salario} = {porcento}\n',
          f'emprestimo / porcendo = {prestacao:.1f} meses')
