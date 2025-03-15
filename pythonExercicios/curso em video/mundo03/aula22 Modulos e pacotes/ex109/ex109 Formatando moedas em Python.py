# ======================================================================================================================
# Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parametro a mais,
# informando se o valor retornado por elas vai ser ou não formatado pela função moeda desenvolvida no desafio 108.
# ======================================================================================================================
import moeda

aum = 10
des = 13
preco = float(input("digite o preço: R$"))
print(f'A metade de {moeda.moeda(preco)} é {moeda.metade(preco, )}\n'
      f'O dobro de {moeda.moeda(preco)} é {moeda.dobro(preco, )}\n'
      f'Aumentando em {aum}%, resulta em {moeda.aumentar(preco, aum, )}\n'
      f'Reduzindo em {des}%, resulta em {moeda.diminuir(preco, des, )}')

# f
