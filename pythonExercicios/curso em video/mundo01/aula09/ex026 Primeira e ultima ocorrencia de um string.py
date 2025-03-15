print('''

      ==================================================
      Faça um programa que leia um frase pelo teclado
      e mostre:
      -Quantas vezes aparece a letra "A"
      -Em que posiçao ela aparece a primeira vez
      -Em que posiçao ela aparece a ultima vez
      ==================================================
      ''')
######################################################################
######################################################################
frase = str(input('(vou remover espaços desnecessarios antes e depois)\n'
                  'Digite uma frase: ')).strip()
msg = frase.upper()
s = msg.find('A')
e = msg.rfind('A')
print(f'Na frase: "{frase}"\n'
      f'A letra "a" aparece {msg.count("A")} vezes\n'
      f'pela primeira vez na posição {msg.find("A") + 1}\n'
      f'pela ultima vez na posição {msg.rfind("A") + 1}')
