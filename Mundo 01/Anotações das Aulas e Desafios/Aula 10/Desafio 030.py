"""
DESAFIO 030: Par ou Ímpar?

Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
"""
num = int(input('Digite um número inteiro (ex: 55): '))
if num % 2 == 0:
    print('{} é um número par!'.format(num))
else:
    print('{} é um número ímpar!'.format(num))
