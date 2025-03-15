# ======================================================================================================================
# Crie um programa que tenha uma função chamada voto() que vai receber como parametro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATORIO nas eleiçoes
# ======================================================================================================================
def voto(nasc):
    from datetime import date
    idade = date.today().year - nasc
    if idade < 16:
        return f'com {idade} anos de idade: NÃO VOTA'
    elif 16 <= idade < 18 or 65 < idade:
        return f'com {idade} anos de idade: {C["B"]}VOTO OPCIONAL{C[""]}'
    elif 18 <= idade < 65:
        return f'com {idade} anos de idade: {C["R"]}VOTO OBRIGATORIO{C[""]}'


# ╔════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║                                                    MAIN PROGRAM                                                    ║
# ╚════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
C = {"": '\033[minutos',
     "R": '\033[31m',
     "B": '\033[35m'}

print(voto(int(input('ano de nascimento: '))))

# fim
