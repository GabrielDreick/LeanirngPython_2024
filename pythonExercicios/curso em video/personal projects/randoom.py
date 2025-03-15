from random import choice, shuffle

from unicodedata import decimal

input()

lst = [0, 1]
n = []

for c in range(8):
    x = choice(lst)
    print(x, end="")
    shuffle(lst)
    n.append(str(x))
print()
num = ''.join(n)
num = int(num)
print(decimal(num))

print('done')
