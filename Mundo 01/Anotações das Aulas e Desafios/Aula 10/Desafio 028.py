"""
DESAFIO 028: Jogo da Adivinhação v1.0

Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""
from random import randint
nr = randint(0, 5)
ad = int(input('Adivinhe qual número eu estou pensando (digite um número de 0 a 5): '))
if ad == nr:
    print('Parabéns, você acertou! Eu estava pensando no número {}.'.format(nr))
else:
    print('Você errou! Eu estava pensando no número {}.'.format(nr))
