"""
DESAFIO 046: Contagem Regressiva

Faça um programa que mostre na tela uma contagem regressiva para o estouro de
fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
"""
from time import sleep
print('Contagem regressiva para estourar os fogos de artifício:')
for c in range(10, 0 - 1, -1):
    sleep(1)
    if c != 0:
        print('{}...'.format(c))
    else:
        print('BOOOM!')
