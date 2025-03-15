def leiaDinheiro(txt):
    while True:
        entrada = str(input(txt)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == "":
            print(f'\033[31mErro: {entrada} não é um preço valido\033[m')
        else:
            return float(entrada)
