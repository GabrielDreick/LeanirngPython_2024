# ======================================================================================================================
# Faça um mini-sistema que utilize o Interactiove Help do Python.
# O usuario vai digitar o comando e o manual vai aparecer.
# Quando o usuario digitar a palavra 'FIM', o program se encerrará.
#
# OBS: use cores.
# ======================================================================================================================

while True:
    desc = str(input('Descrição de qual função: '))
    if desc.strip().upper() == 'FIM':
        print('encerrando...')
        break
    else:
        print('\n'*30)
        print('\033[33m')
        help(desc)
        print('\033[0m')

# fim
