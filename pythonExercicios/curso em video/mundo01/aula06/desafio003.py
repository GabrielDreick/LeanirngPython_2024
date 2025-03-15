print()
print()
print('========================================')
print('Crie um programa que leia dois números e')
print('mostre a soma entre eles.')
print('========================================')
print()

n1 = float(input('Digite um numero: '))
n2 = float(input('Digite mais um número: '))
s = n1 + n2


if n1 == int(n1):
    n1 = int(n1)

if n2 == int(n2):
    n2 = int(n2)

if s == int(s):
    s = int(s)


print(f'A soma entre {n1} e {n2} vale {s}.')
