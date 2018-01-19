"""
DESAFIO 052: Números Primos

Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
"""
n = int(input('Digite um número: '))
v = True

if n < 2:
    v = False
else:
    for c in range(2, n - 1):
        if n % c == 0:
            v = False

if v:
    print('{} é um número primo.'.format(n))
else:
    print('{} não é um número primo.'.format(n))
