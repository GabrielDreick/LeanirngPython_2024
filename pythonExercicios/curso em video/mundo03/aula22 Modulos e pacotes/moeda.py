# ======================================================================================================================
# Crie um módulo chamado moeada.py que tenha as funções incorporadas
# aumentar(), diminuir(), dobro(), e metade().
#

def aumentar(num, n, format=True):
    num += (n * num / 100)
    if format:
        num = moeda(num)
    return num


def diminuir(num, n, format=True):
    num = num - (n * num / 100)
    if format:
        num = moeda(num)
    return num


def dobro(num, format=True):
    num *= 2
    if format:
        num = moeda(num)
    return num


def metade(num, format=True):
    num /= 2
    if format:
        num = moeda(num)
    return num


def moeda(num):
    num = f"{num:.2f}"
    return num


def resumo(num, aumento=0, desconto=0, format=True):
    print('=' * 40)
    print(f'{f"referente ao valor: R${moeda(num)}":^40}')
    print('=' * 40)
    print(f'{f"O Dobro é: "}{f"R${dobro(num, format)}"}\n'
          f'{f"A Metade é: "}{f"R${metade(num, format)}"}\n'
          f'{f"Aumentando em {aumento}%, dá: "}{f"R${aumentar(num, aumento, format)}"}\n'
          f'{f"Reduzindo em {desconto}%, dá: "}{f"R${diminuir(num, desconto, format)}"}')
    print('=' * 40)

