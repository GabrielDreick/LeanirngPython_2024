# ======================================================================================================================
# Melhore o DESAFIO 061, perguntando para o usuario se ele quer mostrar mais alguns termos.
# o programa encerra quando ele disser que quer 0 termos.
# ======================================================================================================================
print('')
primeiro = int(input('Primeiro termo: '))
num = primeiro
razao = int(input('E a Razão '))
pa = 10
total = 10
print()
while pa != 0:
    print(num, end='  ')
    num = num + razao
    pa = pa - 1

    if pa == 0:
        pa = int(input('\nMais quantos termos? (0 encerra) '))
        print()
        total = total + pa
print(f'foram mostrados {total} termos.')

# fim
