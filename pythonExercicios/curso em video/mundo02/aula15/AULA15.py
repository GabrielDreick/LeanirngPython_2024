from random import randint
from time import sleep
n = 0
while True:
    print(n)
    n += 1
    sleep(.05)
    if n == randint(24, 142):
        break
