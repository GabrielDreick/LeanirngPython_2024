
#   style   back
# \033[0;33;44m
#       text

# STYLE
# 0 none
# 1 bold
# 4 underline
# 7 negative
#
# TEXT
# 30 white
# 31 red
# 32 green
# 33 yellow
# 34 blue
# 35 magenta
# 36 teal
# 37 grey
#    black possible
#
# BACK
# 40 white
# 41 red
# 42 green
# 43 yellow
# 44 blue
# 45 magenta
# 46 teal
# 47 grey

print('\033[0;31mTeste\033[minutos')
print('\033[4;31mTeste\033[minutos')
print('\033[1;31mTeste\033[minutos')
print('\033[42mTeste\033[minutos')
print('\033[32mTeste\033[minutos')
print('\033[7;30;41mTeste\033[minutos')
'''
cores = {'limpa' : '\033[minutos',
         'vermelho' : '\033[31m',
         'verde' : '\033[32m',
         'censura' : '\033[7;30;40m',
         'marcado' : '\033[7;30;41'}'''
cores = {0: '\033[minutos',
         1: '\033[32m',
         2: '\033[31m',
         3: '\033[7;30;40m',
         4: '\033[7;30;41m'}

from time import sleep


def my_print(txt=''):
    for c in txt:
        sleep(.22)
        print(c, end='')
    print()


sleep(3)
print(f"{cores[1]}hello{cores[0]}")
sleep(.8)
print("i'minutos not gonna try to be fancy, with lots of thought out text...")
sleep(2.2)
print("but...")
sleep(2.3)
print("...well...")
sleep(1.8)
print("...")
sleep(4.2)
print("wait...")
sleep(6.3)
print(f"i can use {cores[3]}sleep(){cores[0]} to make this more...")
sleep(2.7)
my_print(f"...{cores[2]}Interesting{cores[0]}.")
sleep(1.9)
print('...')
sleep(8.9)
my_print("...yes... this way we'll have...")
sleep(1.7)
my_print('so...')
sleep(1.3)
my_print(f'{cores[2]}...much...{cores[4]}')
sleep(1.3)
print('          ', end="")
my_print('FUN HEHEHAHAHAHAHA')
