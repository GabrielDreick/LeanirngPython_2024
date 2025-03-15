from time import sleep
from datetime import datetime

horas = datetime.today().hour
minutos = datetime.today().minute
segundos = datetime.today().second

print('\n' * 30, f'{horas}:{minutos}.{segundos}')

while True:
    segundos += 1
    print('\n' * 30, f'{horas}:{minutos}.{segundos}')
    if segundos == 60:
        segundos = 0
        minutos += 1
    if minutos == 60:
        minutos = 0
        horas += 1
    sleep(1)
