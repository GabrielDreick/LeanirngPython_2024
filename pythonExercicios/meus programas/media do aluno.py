from time import sleep

C = {"": "\033[0m"}

dados = {}
media = 0

dados["nome"] = str(input("Nome: ")).strip()
quantasNotas = int(input('Quantas nota serão registradas?\n'
                         '>'))
for c in range(1, quantasNotas + 1):
    dados[f"nota{c}"] = float(input(f"{c}ª nota: "))
    media += dados[f"nota{c}"]
media = media / quantasNotas
dados["media"] = media

if dados["media"] > 6.9:
    cor = "\033[38;2;100;200;100m"
    resultado = "APROVADO"
elif 7 > dados["media"] >= 5:
    cor = "\033[38;2;200;200;100m"
    resultado = "RECUPERAÇÃO"
elif dados["media"] < 5:
    cor = "\033[38;2;200;100;100m"
    resultado = "REPROVADO"

print(dados)
print('\n' * 20)

time = .22

print('=' * 30)
sleep(time)
print(f'Nome: {dados["nome"]}')
sleep(time)
for c in range(1, quantasNotas + 1):
    print(f'{c}ª Nota: {dados[f"nota{c}"]}')
    sleep(time)
print(f'Media: {cor}{dados["media"]} - {resultado}{C[""]}')
sleep(time)
print('=' * 30)
