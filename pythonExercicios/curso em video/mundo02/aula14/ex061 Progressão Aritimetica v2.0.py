# ======================================================================================================================
# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão
# usando a estrutura while.
# ======================================================================================================================
primeiro = int(input('Primeiro termo: '))
num = primeiro
razao = int(input('E a Razão '))
pa = 10

while pa != 0:
    print(num, end='  ')
    num = num + razao
    pa = pa - 1

# fim
