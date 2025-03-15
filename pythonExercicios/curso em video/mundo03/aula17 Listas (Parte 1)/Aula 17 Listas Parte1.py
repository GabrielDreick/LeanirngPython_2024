c = '\033[32m'
v = '\033[0m'

lanche = ['hamburger', 'suco', 'pizza', 'pudim']            # cria uma lista
print(f'{c}lanche ={v}', lanche)
print()
lanche.append('cookie')                                     # adiciona 'cookie' ao final
print(f'{c}append(cookie){v}', lanche)
print()
lanche.insert(0, 'cachorro-quente')                         # insere 'cachorro-quente' na posição 0
print(f'{c}insert("hotdog"){v}', lanche)
print()
del lanche[3]                                               # deleta o que esta na posição 3
print(f'{c}del [3]{v}', lanche)
print()
lanche = ['hamburger', 'suco', 'pizza', 'pudim']
lanche.append('cookie')
lanche.insert(0, 'cachorro quente')
lanche.pop(3)                                               # .pop() elimina o ultimo, mas da para especificar .pop(x)
print(f'{c}undo; .pop(3){v}', lanche)
print()
lanche = ['hamburger', 'suco', 'pizza', 'pudim']
lanche.append('cookie')
lanche.insert(0, 'cachorro quente')
lanche.remove('pizza')                                      # remove o primeiro 'pizza' que encontrar
print(f'{c}undo; .remove(pizza){v}', lanche)                # se nao existir, vai dar erro, use {if 'pizza' in...}
print()
valores = list(range(4, 11))
print(valores)
print()
valores = [8, 2, 5, 4, 9, 3, 0]
print(valores)
print()
valores.sort()                                              # organiza de forma crescente
print(valores)
print()
valores.sort(reverse=True)                                  # organiza de forma decrescente
print(valores)
print()
print(len(valores))
print()
valores[2] = 1000                                           # subistitui o valor na posição 2 pelo valor '1000'
print(valores)

valores = []
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for pos, val in enumerate(valores):
    print(f'Na posição {pos} tem o valor {val}')

a = [2, 3, 4, 7]
b = a
b[2] = 8                                                    # no Python, se uma lista recebe outra, na verdade, elas
print(f'lista A: {a}')                                      # INTERLIGAM...
print(f'lista B: {b}')
print()
a = [2, 3, 4, 7]
b = a[:]                                                    # mas com [:], ele vai ler do início ao fim
b[2] = 8                                                    # e COPIAR para o B
print(f'lista A: {a}')
print(f'lista B: {b}')
