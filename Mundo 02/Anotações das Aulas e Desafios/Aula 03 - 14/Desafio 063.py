"""
DESAFIO 063: Sequência de Fibonacci v1.0

Escreva um programa que leia um número n inteiro qualquer e mostre
na tela os n primeiros elementos de uma Sequência de Fibonacci.

Ex: 0 → 1 → 1 → 2 → 3 → 5 → 8
"""

"""
# Feito com for
x = 1
y = 0

n = int(input('Digite quantos primeiros elementos da Sequência de Fibonacci você quer exibir: '))

if n > 0:
    if n == 1:
        print('0')
    else:
        print('0', end=' → ')

    for i in range(1, n):
        z = x + y
        if i == n - 1:
            print(z, end='')
        else:
            print(z, end=' → ')
        x = y
        y = z
"""

# Feito com while
contador = 1
x = 1
y = 0

n = int(input('Digite quantos primeiros elementos da Sequência de Fibonacci você quer exibir: '))

if n > 0:
    if n == 1:
        print('0')
    else:
        print('0', end=' → ')

    while contador < n:
        z = x + y
        if contador == n - 1:
            print(z, end='')
        else:
            print(z, end=' → ')
        x = y
        y = z
        contador += 1
