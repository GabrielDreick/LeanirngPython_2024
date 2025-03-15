# ======================================================================================================================
# desenvolva um programa que leia SEIS NUMEROS INTEIROS e mostre a soma apenas daqueles que forem PARES.
# se o valor digitado for IMPAR, desconsidere-o.
# ======================================================================================================================
print('Vou pedir seis numeros inteiros e vou soma-los usando uma condinção que so vou revelar no final')
soma = 0
contador = 0
for par in range(1, 7):
    num = int(input(f'{par}º Numero: '))
    if num % 2 == 0:
        contador += 1
        soma = soma + num

print(f'A soma dos {contador} numeros pares que você digitou dá: {soma}. (a condição era "numeros pares")')

# fim
