# ======================================================================================================================
# Crie um program que tenha uma função fatorial() que receba dois parametros:
# o primeiro que indique o numero a calcular e o outro chamado show, que sera um valor logico (opcional)
# indicando se sera mostrado ou não na tela de processo de calculo do fatorial
# ======================================================================================================================
def fatorial(num, show=False):
    """
    :param num: numero para calcular o fatiorial
    :param show: 'N' = não mostrar o calculo, 'S' = mostrar o calculo
    :return: retorna o fatorial
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end="")
            if c > 1:
                print(f' x ', end='')
            else:
                print(f' = {f}')
        f *= c
    return f


# ╔════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║                                                    MAIN PROGRAM                                                    ║
# ╚════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
n = 5
f = fatorial(n, True)
print(f'o fatorial do numero {n} é {f}')

# fim
