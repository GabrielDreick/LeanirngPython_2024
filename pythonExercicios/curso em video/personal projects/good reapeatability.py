from random import choice

msgEntendo = ['aaah, entendi, é, faz sentido.', 'ah sim, ta certo.', 'ah... agora eu vejo.']
msgNaoEntendo = ['hmm... não... não entendi.', 'ãããh...', 'não entendo.']


for c in range(0, 3):
    print(choice(msgNaoEntendo), '   ', choice(msgEntendo))
