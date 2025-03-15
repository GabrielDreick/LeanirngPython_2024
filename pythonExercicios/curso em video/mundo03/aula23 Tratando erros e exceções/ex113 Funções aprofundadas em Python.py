# ======================================================================================================================
# Reescreva a função leiaInt() que fizemos no desafio 104,
# incluindo agora a possibilidade da digitação de um numero de tipo invalido.
# Aproveite e crie tambem a função leiaFloat() com a mesma funcionalidade.
# ======================================================================================================================
def leiaInt(txt):
    while True:
        try:
            i = int(input(txt))
        except KeyboardInterrupt:
            print('\033[38;2;255;100;100mO Usuario descidiu não digitar o numero\033[minutos')
            return 0
        except:
            print("\033[38;2;255;75;75mDigite um numero \033[38;2;200;200;50minteiro\033[38;2;255;75;75m valido\033[minutos")
        else:
            return i


def leiaFloat(txt):
    while True:
        try:
            f = float(input(txt))
        except KeyboardInterrupt:
            print('\033[38;2;255;100;100mO Usuario descidiu não digitar o numero. inserindo 0\033[minutos')
            return 0
        except:
            print("\033[38;2;255;0;0mDigite um numero \033[38;2;255;255;0mreal\033[38;2;255;0;0m valido\033[minutos")
        else:
            return f


# ╔════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║                                                    MAIN PROGRAM                                                    ║
# ╚════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
i = leiaInt("Digite um numero inteiro: ")
f = leiaFloat("Digite um numero real: ")
print(f"Voce digitou o numero inteiro {i} e o numero real {f}")

# fim
