# ======================================================================================================================
# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os(com idade) em um dicionario se
# por acaso a CTPS for diferente de ZERO, o dicionario recebera tambem o ano de contratação e o solário.
# Calcule e acrescente, alem da idade, com quanto anos a pessoa vai se aposentar. (35anos de contibuição para aposentar)
# ======================================================================================================================
from datetime import date

hoje = date.today().year

print('\n' * 30)

for c in '|||V            ':
    print(c)
dados = {}
dados["nome"] = str(input("Nome: ")).strip().title()
dados["idade"] = hoje - int(input("Ano de Nascimento: "))
dados["ctps"] = int(input("Carteira de Trabalho (0 = não tem): "))
if dados["ctps"] != 0:                      # diferente pode ser numero negativo, tem com ter ctps negativa?
    dados["contratado"] = int(input("Ano de Contratação: "))
    dados["salario"] = float(input("Salario: R$"))
    dados["aposentadoria"] = (dados["idade"] + ((dados["contratado"] + 35) - hoje))


print('\n' * 30)
print('=' * 30)
print(f'Nome: {dados["nome"]}\n'
      f'Idade: {dados["idade"]}\n'
      f'Carteira de Trabalho: {dados["ctps"]}')
if dados["ctps"] != 0:
    print(f'Ano de Contratação: {dados["contratado"]}\n'
          f'Salario: R${dados["salario"]}\n'
          f'Idade de Aposentadoria: {dados["aposentadoria"]}')
print('=' * 30)
# fim
