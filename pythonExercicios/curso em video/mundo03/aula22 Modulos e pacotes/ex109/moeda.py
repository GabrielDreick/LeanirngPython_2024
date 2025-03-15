def aumentar(preco=0.0, taxa=0, formatar=True):
    res = preco + (preco * taxa/100)
    if formatar:
        return moeda(res)
    else:
        return res


def diminuir(preco=0.0, taxa=0, formatar=True):
    res = preco - (preco * taxa / 100)
    if formatar:
        return moeda(res)
    else:
        return res


def dobro(preco=0.0, formatar=True):
    res = preco * 2
    if formatar:
        return moeda(res)
    else:
        return res

def metade(preco=0.0, formatar=True):
    res = preco / 2
    if formatar:
        return moeda(res)
    else:
        return res


def moeda(preco=0.0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')
