def soma(a, b):
    s = a + b
    print(f'a soma de {a} + {b} = {s}')


def somax(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'somando {valores}, o resultado é {s}')


def contador(*num):
    for valor in num:
        print(valor, end=' ')
        print()


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


#  PROGRAMA PRINCIPAL =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=0=0=0=0=0=0=0=0=0=0=0=0=0=0=0=0
soma(a=4, b=5)
soma(b=8, a=9)
soma(2, 1)
somax(8, 7, 9, 6, 5)
contador(1, 2, 3, 4)

valores = [7, 2, 5, 0, 4]
print(valores)
dobra(valores)
print(valores)
