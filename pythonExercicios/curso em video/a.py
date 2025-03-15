


# calculando:
# -area = largura * altura
# -porcentagem = ('%' * x) / 100
#
#





# aula 7
# ordem de precedencia
#       1 ()
#       2 **
#       3 *, /, //, %
#       4 +, -
#
#       // divisao inteira
#       % resto da divisao
#
#     raiz quadrada
#      x ** 0.5
#
# em calculo .format, {num:.3f} limita o float para 3 digitos
#
nome = 'Gabriel'
print(f'ola    {nome:20}!')
print(f'ola  > {nome:>20}!')
print(f'ola  < {nome:<20}!')
print(f'ola  ^ {nome:^20}!')
print(f'ola =^ {nome:=^20}!')
print(f'ola _^ {nome:_^20}!')

print()
print('se no final da linha do print terminar com , end=" ")', end=' ')
print(', o proximo print nao vai quebrar a linha')

print()
print('e se eu quiser\n quebrar a linha\n sem mais print\n eu uso (alt+92)"\ n" juntos')

# Aula 8
#
# math.hypot(co, ca)
#
# math.sin(math.radians(x))
# math.cos(math.radians(x))
# math.tan(math.radians(x))
#
# lista [1, 2, 3, 4...]
# random.choice(lista)
# >>2
#
#
# lista = [1, 2, 3, 4...]
# random.shuffle(lista)
#
# >>2 4 1 3
#
#
# import pygame
# pygame.init()
# pygame.mixer.music.load('filename.mp3')
# pygame.mixer.music.play()
# input   ### so it will play it before finishing the program
#
#
# Aula9
# frase  = 'Curso em Video Python'
# print(frase[9:13])
# >> Vide    9 é o inicio, 13 é o final - 1
#
# prin
#
#
# aula10
#
# from datetime import date
# date.today().year     # pega o ano contado na maquina
#
#
#

# a = open(nome, 'rt')   'r' = read; 't' = text
# a = open(nome, 'wt+')  'w' = write; 't' = text; '+' = create
# a.close()



# <r> antes da string tranforma em raw string: contra-barras nao causam problemas
# caminho = r"C://Users\joao\Downloads\nova"

# 24h  24m 24s
# 24h  12m 12s
# 24h   6m 60s
# 24h   3m 60s
# 24h 1.5m 60s


# gui:
# tkinter
# wxPython
# PyQt
#
# streamlit  https://docs.streamlit.io/library/cheatsheet

# pyscript stackoverflow.com/questions/73682009

x = 2
y = 4

x = x / y
print(x)

y = y / x


print(y)