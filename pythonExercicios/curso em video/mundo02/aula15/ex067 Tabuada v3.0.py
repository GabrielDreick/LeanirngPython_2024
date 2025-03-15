# ======================================================================================================================
# Faça um programa que mostre a tabuada de varios numeros, um de cada vez, para cada valor digitado pelo usuario.
# O programa sera interrompido quando o numero solicitado for negativo.
# ======================================================================================================================
print('Irei te mostrar a tabuada do numero(inteiro) que você der, digite um numero negativo para encerrar.')
while True:
    n = int(input('(numero negativo = encerrar)\n'
                  'Tabuada para o numero: '))
    if n < 0:
        break
    print(f'┌TABUADA DE {n:─<4}────┐')
    for c in range(1, 11):
        print(f'│ {n:>4} x {c:>2} = {n*c:>4}  │')
    print('└───────────────────┘')

# fim
