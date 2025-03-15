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


def resumo(preco=0.0, aumento=0, desconto=0, formatar=True):
    print('═'*40)
    print(f'{f"Resumo do valor {moeda(preco)}":^40}')
    print('═'*40)
    print(f' Dobro do preço: \t{dobro(preco, formatar)}\n'
          f' Metade do preço: \t{metade(preco, formatar)}\n'
          f' Aumento de {aumento}%: \t{aumentar(preco, formatar)}\n'
          f' Desconto de {desconto}%: \t{diminuir(preco, formatar)}')
    print('═'*40)
