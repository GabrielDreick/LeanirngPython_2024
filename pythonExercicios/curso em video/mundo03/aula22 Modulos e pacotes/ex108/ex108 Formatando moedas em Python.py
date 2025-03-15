# ======================================================================================================================
# Adapte o codigo do desafio 107, criando uma função adicional chamada moeada() que consiga mostrar os valores como um
# valor motenário formatado.
# ======================================================================================================================
import moeda

aum = 10
des = 13
preco = float(input("digite o preço: R$"))
print(f'A metade de {moeda.moeda(preco)} é {moeda.moeda(moeda.metade(preco))}\n'
      f'O dobro de {moeda.moeda(preco)} é {moeda.moeda(moeda.dobro(preco))}\n'
      f'Aumentando em {aum}%, resulta em {moeda.moeda(moeda.aumentar(preco, aum))}\n'
      f'Reduzindo em {des}%, resulta em {moeda.moeda(moeda.diminuir(preco, des))}')

# fim
