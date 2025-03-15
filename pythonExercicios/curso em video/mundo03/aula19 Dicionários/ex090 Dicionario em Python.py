# ======================================================================================================================
# Faça um programa que leia nome e media de um aluno, guardando tambem a situação em um dicionario.
# No final, mostre o conteudo da estrutura na tela
# ======================================================================================================================
aluno = {'nome': str(input('Nome: ').title()), 'media': float(input('Media: '))}
if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 7 > aluno['media'] >= 5:
    aluno['situação'] = 'Recuperação'
elif 5 > aluno['media']:
    aluno['situação'] = 'Reprovado'

print('\n' * 30)
print('=' * 26)
print(f'Nome: {aluno["nome"]}\n'
      f'Media: {aluno["media"]}\n'
      f'Situação: {aluno["situação"]}')
print('=' * 26)

# fim
