from time import sleep

makina = input('so aperta enter')

p = "\033[minutos"
k = p
m = " "
n = 0
s = .3
ha = 'oi'
# for c in range(#partida, #chegada(-1), [-1(decresce, regressa), 2(pula de dois em dois)])
#
if makina:
    for c in range(0, 150):   # para antes do ultimo numero
        if 10 <= n < 50:
            s = .20
            k = '\033[31m'
        if 50 <= n < 110:
            s = .1
            k = '\033[7;30;41m'
        if n >= 110:
            p = k
            ha = 'HA'
        n = n + 1
        print(f'{m*n}{k}{ha}{p}')
        sleep(s)

soma = 0
for c in range(0, 10):
    num = int(input('Digite um numero: '))
    soma += num                                  # eu não gostei deste formato
print(f'a soma de tudo deu {soma}')

