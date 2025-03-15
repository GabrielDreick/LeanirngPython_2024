# ======================================================================================================================
# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você déve mostrar, para cada palavra, quais são a suas vogais.
# ======================================================================================================================
from time import sleep

palavras = ('Ola.', 'toda', 'essas', 'minhas', 'palavras', 'estao', 'dentro', 'de', 'uma', 'tupla,',
            'e', 'agora', 'eu', 'vou', 'te', 'dizer', 'as', 'vogais', 'de', 'cada.')

for intro in range(0, len(palavras)):
    if '.' in palavras[intro] or ',' in palavras[intro]:
        fim = '\n'
    else:
        fim = ' '
    print(palavras[intro], end=fim)
input('[enter]')

for vogais in palavras:
    print(f'\nna palavra ´´{vogais}`` tem as vogais:__________', end='')
    for vogal in vogais:
        if vogal.lower() in 'aeiou':
            print(vogal, end=' ')
'''        if 'a' in vogais:
            print('a', end=' ')
        if 'e' in vogais:
            print('e', end=' ')
        if 'i' in vogais:
            print('i', end=' ')
        if 'o' in vogais:
            print('o', end=' ')
        if 'u' in vogais:
            print('u', end=' ')
        print(end='\n')
        sleep(1.76)
        break'''
print('fwiu. acho que foram todas.')
sleep(1.89)
print('bom, terminei.')
sleep(1.23)
print('tchau')
if input() == 'tchau':
    print(':)')
sleep(.65)

# fim
