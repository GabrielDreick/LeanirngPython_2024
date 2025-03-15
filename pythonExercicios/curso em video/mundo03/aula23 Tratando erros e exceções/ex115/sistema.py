from time import sleep
from lib.interface import *
from lib.arquivo import *

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)
    sleep(1)

while True:
    resposta = menu(['Listar Pessoas', 'Cadastrar Pessoa', 'Sair do Programa'])

    if resposta == 1:  # listar
        lerArquivo(arq)
        input('[enter]')

    elif resposta == 2:  # resistrar
        cabeçalho('Cadastrar', '\033[33m', False)
        nome = str(input('Nome: ')).strip().title()
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
        sleep(2)

    elif resposta == 3 or resposta is None:
        print('Encerrando...')
        sleep(1)
        break

    else:
        print(f'{Color["error"]}Opção desconhecida\033[0m')
        sleep(1)

# fim
