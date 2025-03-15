# ======================================================================================================================
# Crie um módulo chamado moeada.py que tenha as funções incorporadas
# aumentar(), diminuir(), dobro(), e metade().
#
# Faça também um program que importe esse módulo e use algumas dessas funções.
# ======================================================================================================================
import moeda

aum = 10
des = 13
preco = float(input("digite o preço: R$"))
print(f'A metade de {preco} é {moeda.metade(preco)}\n'
      f'O dobro de {preco} é {moeda.dobro(preco)}\n'
      f'Aumentando em {aum}%, resulta em {moeda.aumentar(preco, aum)}\n'
      f'Reduzindo em {des}%, resulta em {moeda.diminuir(preco, des)}')

# fim
