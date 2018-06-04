"""
DESAFIO 074: Maior e Menor Valores em Tupla

Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o
maior valor que estão na tupla.
"""
from random import randint
i, f = 1, 100
a, b, c, d, e = randint(i, f), randint(i, f), randint(i, f), randint(i, f), randint(i, f)
numeros = (a, b, c, d, e)
print(f'Os valores sorteados foram: {numeros}')
print(f'O maior valor sorteado foi {max(numeros)}.')
print(f'O menor valor sorteado foi {min(numeros)}.')
