"""
DESAFIO 016: Quebrando um Número

Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.

Ex:
Digite um número: 6.127
O número 6.127 tem a parte inteira 6.
"""
n = float(input('Digite um Número Real (ex: 6.127): '))
nr = int(n)
print('\nO número inteiro de {} é {}!'.format(n, nr))
