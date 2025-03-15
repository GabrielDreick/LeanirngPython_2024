# ======================================================================================================================
# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
# de acordo com a média atingida:
#
# -Média abaixo de 5.0: REPROVADO
# -Média entre 5.0 e 6.9: RECUPERAÇÃO
# -Média 7.0 ou superior: APROVADO
# ======================================================================================================================
########################################################################################################################
c = {"": '\033[minutos',
     'g': '\033[32m',
     'y': '\033[33m',
     'r': '\033[31m'}

nota1 = float(input('Primeira nota do aluno: '))
nota2 = float(input('Segunda nota do aluno: '))

media = (nota1 + nota2) / 2

if media >= 7:
    print(f'Média: {media:.1f} {c["g"]}APROVADO{c[""]}')
elif 5 <= media < 7:
    print(f'Média: {media:.1f} {c["y"]}RECUPERAÇÃO{c[""]}')
elif media < 5:
    print(f'Média: {media:.1f} {c["r"]}REPROVADO{c[""]}')
else:
    print('\033[37m...eeeerrrrrrrroooooo.....\033[minutos')