# ======================================================================================================================
# Crie um pacote chama de utilidadesCeV que tenha dois modulos internos chamados moeda e dado.
#
# Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.
# ======================================================================================================================
from utilidadesCeV import moeda

aum = 10
des = 13
preco = float(input("Digite um valor: R$"))
moeda.resumo(preco, aum, des, formatar=True)

# f
