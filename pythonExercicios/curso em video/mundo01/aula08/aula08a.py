import random
from math import sqrt, trunc

num = int(input('Digite minutos número: '))
raiz = sqrt(num)

print(f'A raiz de {num} é igual a {raiz:.2f}')

n = random.randint(trunc(raiz), num)
print(n)