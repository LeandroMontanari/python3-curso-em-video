"""
EXERCÍCIO 025: Procurando uma String Dentro de Outra

Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
"""
nome = str(input('Qual é seu nome completo? ')).strip()
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))
