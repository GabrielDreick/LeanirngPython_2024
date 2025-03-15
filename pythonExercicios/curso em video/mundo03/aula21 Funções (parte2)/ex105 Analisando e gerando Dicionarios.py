# ======================================================================================================================
# Faça um programa que tenha uma função notas() que pode receber varias de alunos e vai retornar um dicionario com as
# seguintes informações:
#
# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A media da turma
# - A situação (opcional)
#
# Adicione tambem as docstrings da função
# ======================================================================================================================
def notas(*num, sit=False):
    """
    recebe multiplos numeros para determinar: quantas notas, qual nota é a maior e qual é a menor, a media, e a situação
    :param num: recebe multiplas notas
    :param sit: decide se mostrara a situação como: boa, razoavel ou ruim. Padrão=False
    :return: retorna um dicionario com todas as informações.
                Chaves: "Quantas Notas", "Maior", "Menor", "Media" e, se sit = True, "Situação"
    """
    dict_notas = {"Quantas Notas": len(num), 'Maior': max(num), 'Menor': min(num), 'Media': sum(num)/len(num)}
    if sit:
        if dict_notas['Media'] >= 7:
            dict_notas['Situação'] = 'Boa'
        elif dict_notas['Media'] >= 5:
            dict_notas['Situação'] = 'Razoavel'
        elif dict_notas['Media'] < 5:
            dict_notas['Situação'] = 'Ruim'
    return dict_notas


# ╔════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║                                                    MAIN PROGRAM                                                    ║
# ╚════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
resp = notas(9, 10, 5.5, 2.5, 8.5, sit=True)
help(notas)
print(resp)

# fim
