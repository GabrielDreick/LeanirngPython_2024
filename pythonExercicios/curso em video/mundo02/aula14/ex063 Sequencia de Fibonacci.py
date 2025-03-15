# ======================================================================================================================
# Escreva um programa que leia um número n inteiro qualquer e
# mostre na tela os n primeiros elementos de uma sequência de fibonacci.
#
# Ex:
# 0 > 1 > 1 > 2 > 3 > 5 > 8
# ======================================================================================================================
n = int(input('Quantos numeros da sequencia Fibonacci eu devo te mostrar? >'))
nAnterior = 1
nAtual = 0
fibonacci = 0
while n > 0:
    print(nAtual, end=' ')
    fibonacci = nAtual + nAnterior
    nAnterior = nAtual
    nAtual = fibonacci
    n = n - 1
# fim
