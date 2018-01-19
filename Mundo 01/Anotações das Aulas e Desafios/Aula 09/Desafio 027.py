"""
DESAFIO 027: Primeiro e Último Nome de uma Pessoa

Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro
e o último nome separadamente.

Ex: Ana Maria de Souza
Primeiro = Ana
Último = Souza
"""
nome = input('Digite seu nome completo: ').strip().split()
qtd = len(nome)
print('\nSeu primeiro nome é {} e seu último nome é {}!'.format(nome[0], nome[qtd-1]))
