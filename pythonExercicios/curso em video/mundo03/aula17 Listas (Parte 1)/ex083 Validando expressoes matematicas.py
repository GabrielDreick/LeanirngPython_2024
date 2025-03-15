# ======================================================================================================================
# Crie um programa onde o usuario digite uma expressao qualquer que use parenteses.
# Seu aplicativo devera analisar se a expressao passada esta com os parenteses abertos e fechados na ordem correta.
# ======================================================================================================================
# ((a+b)*c) valido
# ((a+b)*c  invalido

# add (, se achar ), .pop, se no final, a lista tiver alguma coisa, é invalida
pilha = []
expressao = str(input('Expressão matematica: '))
for c in expressao:
    if c == '(':
        pilha.append('(')
    elif c == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Parenteses validos')
else:
    print('Parenteses invalidos')
