# ======================================================================================================================
# Crie um programa que leia dois valores e mostre um menu na tela:
#
# [1]Somar
# [2]Multiplicar
# [3]Maior
# [4]Novos Numeros
# [5]Sair do programa
#
# seu programa devera realizar a operação solicitada em cada caso
# ======================================================================================================================
c = {'': '\033[0m',
     '1': '\033[1;38;2;255;0;0m',
     '3': '\033[38;2;255;255;0m',
     'pri': '\033[38;2;255;0;255m',
     'seg': '\033[38;2;255;175;0m'}
print('\n' * 30)
n1 = int(input(f'{c["pri"]}Primeiro{c[""]} numero: '))
n2 = int(input(f'{c["seg"]}Segundo{c[""]} numero: '))

escolha = 0
while escolha != 5:
    print('\n' * 30)
    escolha = int(input(f'{c["pri"]}Primeiro{c[""]} numero: {c["pri"]}{n1}{c[""]}\n'
                        f'{c["seg"]}Segundo{c[""]} numero: {c["seg"]}{n2}{c[""]}\n'
                        '=============================\n'
                        '[1]Somar\n'
                        '[2]Multiplicar\n'
                        '[3]Maior\n'
                        f'[4]{c["3"]}Novos numeros{c[""]}\n'
                        f'[5]{c["1"]}Sair do programa{c[""]}\n'
                        f'============================\n'
                        'Qual você quer? >>'))
    print('\n' * 30)
    if escolha == 1:
        print(f'A soma entre {c["pri"]}{n1}{c[""]} e {c["seg"]}{n2}{c[""]} e igual a {n1+n2}')
        x = input('[enter]')
    elif escolha == 2:
        print(f'A multiplicação entre {c["pri"]}{n1}{c[""]} e {c["seg"]}{n2}{c[""]} e igual a {n1*n2}')
        x = input('[enter]')
    elif escolha == 3:
        if n1 == n2:
            print('sao iguais')
            x = input('[enter]')
        elif n1 > n2:
            print(f'O {c["pri"]}Primeiro{c[""]} numero, {c["pri"]}{n1}{c[""]}, é o maior')
            x = input('[enter]')
        elif n2 > n1:
            print(f'O {c["seg"]}Segundo{c[""]} numero, {c["seg"]}{n2}{c[""]}, é o  maior')
            x = input('[enter]')
    elif escolha == 4:
        n1 = int(input(f'{c["pri"]}Primeiro{c[""]} numero: '))
        n2 = int(input(f'{c["seg"]}Segundo{c[""]} numero: '))
    elif escolha == 5:
        escolha = 9
        while escolha != 0 and escolha != 5:
            print('\n' * 30)
            escolha = int(input('[0]Ficar\n'
                                f'[5]{c["1"]}SAIR{c[""]}\n'
                                'Certeza? >>'))
        if escolha == 5:
            print(f'\n' * 30,
                  f'{c["1"]}Saindo...{c[""]}')
    else:
        print('\n' * 30 +
              'Opção Invalida')
        input('[enter]')

# fim
