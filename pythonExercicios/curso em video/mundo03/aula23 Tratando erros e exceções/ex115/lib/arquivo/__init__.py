from ..interface import *


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('alguma coisa deu errado ao criar o arquivo')
    else:
        print(f'Arquivo [{nome}] criado com sucesso')


def lerArquivo(nome):
    try:
        a = open(nome)
    except:
        print('erro ao ler o arquivo')
    else:
        cabeçalho('Listagem de Pessoas', '\033[36m')
        azul1 = "\033[48;2;25;75;100m"
        azul2 = "\033[48;2;50;125;150m"
        cor = azul1
        for index, linha in enumerate(a):
            if cor == azul1:
                cor = azul2
            elif cor == azul2:
                cor = azul1

            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{cor}{index+1:>3} - {dado[0]:28} {dado[1]:>2} anos\033[48m')


def cadastrar(arq, nome='<nome desconhecido>', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('ERRO. Falha durante a abertura do arquivo.')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('ERRO. Falha durante a gravação no arquivo.')
        else:
            print(f'Novo registro de [{nome}] adicionado.')
            a.close()
