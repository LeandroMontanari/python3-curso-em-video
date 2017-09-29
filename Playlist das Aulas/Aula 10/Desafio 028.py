from random import randint
nr = randint(0, 5)
ad = int(input('Adivinhe qual número eu estou pensando (digite um número de 0 a 5): '))
if ad == nr:
    print('Parabéns, você acertou! Eu estava pensando no número {}.'.format(nr))
else:
    print('Você errou! Eu estava pensando no número {}.'.format(nr))