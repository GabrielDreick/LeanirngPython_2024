# print(x)

# n = int(input('num')) oito
from time import sleep

while True:
    try:
        a = int(input("Numerador: "))
        b = int(input("Denominador: "))
        r = a / b
    # except (ValueError, TypeError):
    #     print("problema com o tipo de dado digitado")
    except ZeroDivisionError:
        print('não da pra dividir por zero')
    # except Exception as erro:
    #     print(f"Erro: {erro.__class__}")
    else:
        print(f'O resultodo é {int(r)}')
        break
    finally:
        print('tick')
        sleep(1)
        print('tock')
        sleep(1)
print('fim')
