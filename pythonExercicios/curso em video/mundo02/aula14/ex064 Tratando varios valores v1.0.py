# ======================================================================================================================
# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# no final, mostre quantos números forem digitados e qual foi a soma entre eles
# (desconsiderando o flag).
# ======================================================================================================================
c = {'': '\033[0m',
     '999': '\033[38;2;255;0;0m',
     '#': '\033[38;2;100;100;100m'}

print(f'Vou somar os numeros que você digitar,\n'
      f'só vou parar quando você digitar o numero [{c["999"]}999{c[""]}]'
      f'{c["#"]}(é, eu pensei ´´e se eu quiser usar o numero [999]``){c[""]}\n')
n = int(input('Numero: '))
contador = somado = 0
while n != 999:
    contador += 1
    somado += n
    n = int(input('Numero: '))

print(f'A soma de todos os {contador} numeros que você digitou dá {somado}')

# fim
