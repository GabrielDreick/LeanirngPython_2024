# ======================================================================================================================
# Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um modulo chamado dado.
# crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função input(),
# mas com uma validação de dados para aceitar apenas valores que sejam monetários.
# ======================================================================================================================
from utilidadesCeV import moeda, dado

aum = 10
des = 13
preco = dado.leiaDinheiro('Digite um valor: R$')
moeda.resumo(preco, aum, des, formatar=True)

# fim
