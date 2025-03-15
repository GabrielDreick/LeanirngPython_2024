# ======================================================================================================================
# Desenvolva um programa que leia o PRIMEIRO TERMO e a RAZÃO de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.
# ======================================================================================================================
print('\n'
      '10 Primeiros Termos de uma PA\n'
      '\033[37m'
      '(conta de 0 ate 10 pulando de 2 em 2: 0,2,4...)\n'
      '(         ^-primeiro termo    ^----^-razão)\033[minutos')

termo = int(input('qual é o primeiro termo? '))
razao = int(input('razão: '))

print(f'Uma progressão aritimetica com o Termo {termo} e a Razão {razao} é:\n')
for pa in range(termo, termo+10*razao, razao):
    print(f'{pa}', end=' ')

'''
decimo = termo = (10 - 1) * razao
for pa in range(termo, decimo + razao, razao):
      print(f'{pa}', end=' ')
'''
