"""
EXERCÍCIO 005: Antecessor e Sucessor

Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.
"""
n = int(input('Digite um número: '))
print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}!'.format(n, (n - 1), (n + 1)))
