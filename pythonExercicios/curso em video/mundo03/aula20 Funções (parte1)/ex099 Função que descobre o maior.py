# ======================================================================================================================
# Faça um programa que tenha uma função camada maior(),
# que receba varios parametros com valores inteiros.
#
# seu programa tem que analisar todos os valores e dizer qual deles é o maior.
# ======================================================================================================================
def maior(*num):
    print('=' * 30)
    print(f'{len(num)} valores entrados.')
    print(f'os valores entrados são:', end=' ')
    mai = cont = 0
    for c in num:
        print(c, end=' ')
        if cont == 0:
            mai = c
            cont += 1
        elif c > mai:
            mai = c
    print(f'\n'
          f'o maior é {mai}')


# programa principal

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
maior(-5, -8, -2)

# fim
