"""
EXERCÍCIO 038: Comparando Números

Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:

- O primeiro valor é maior.
- O segundo valor é maior.
- Não existe valor maior, os dois são iguais.
"""
n1 = int(input('Primeiro número: '))
n2 = int(input('Segunda número: '))
if n1 > n2:
    print('O PRIMEIRO valor é maior!')
elif n2 > n1:
    print('O SEGUNDO valor é maior!')
else:
    print('Os dois valores são IGUAIS!')
