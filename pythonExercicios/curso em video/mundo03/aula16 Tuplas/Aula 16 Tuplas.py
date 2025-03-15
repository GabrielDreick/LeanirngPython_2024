# tupla = ()
# lista = []
# dicionario = {}
#
# ==variavel simples==
# lanche = hamburguer
lanche = 'hamburguer'
# lanche:
#   hamburguer
print(lanche)

# Tupla   0           1     2      3
lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
# lache:
#   hamburguer
#   suco
#   pizza
#   pudim

print(lanche)
print(lanche[2])
print(lanche[0:2])
print(lanche[1:])
print(lanche[-1])
print(len(lanche))

print('\n')
for comida in lanche:
    print(f'vou comer {comida}')
print('\n')
for cont in range(0, len(lanche)):
    print(f'vou comer {lanche[cont]} na posição {cont}')
print('\n')
for pos, comida in enumerate(lanche):
    print(f'vou comer {comida} na posição {pos}')
print('\n')

print(lanche[1:3])
print(lanche[-2:])

print(sorted(lanche))

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
d = b + a
print(a)
print(b)
print(c)
print(d)
print(c.count(5))
print(c)
print('\033[37m 0  1  2  3  4  5  6\033[minutos')
print('achar "8"', c.index(8) + 1)
print('achar "5" a partir da posição "2"', c.index(5, 2))

# tuplas no Python podem ter tipos diferentes juntos
pessoa = ('Gustavo', 39, 'M', 99.88)
print(f'\n'
      f'Nome: {pessoa[0]}\n'
      f'Idade: {pessoa[1]}\n'
      f'Sexo: {pessoa[2]}\n'
      f'Peso: {pessoa[3]}\n')
del pessoa

##################################################
print('\nMUNDANDO TUPLA')  # esse sou eu fazendo
slot1 = str(input('espaço um: '))
slot2 = str(input('espaço dois: '))
slot3 = str(input('espaço tres: '))
slot4 = str(input('espaço quatro: '))
tuplaImutavel = (slot1, slot2, slot3, slot4)
print(tuplaImutavel)
slot1 = str(input('espaço um: '))
slot2 = str(input('espaço dois: '))
slot3 = str(input('espaço tres: '))
slot4 = str(input('espaço quatro: '))
tuplaImutavel = (slot1, slot2, slot3, slot4)
print(tuplaImutavel)
