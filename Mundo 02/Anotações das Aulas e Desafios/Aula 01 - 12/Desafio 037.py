"""
DESAFIO 037: Conversor de Bases Numéricas

Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será
a base de conversão:

- 1 para Binário
- 2 para Octal
- 3 para Hexadecimal
"""
num = int(input('Digite um número inteiro: '))
print('Para qual base você deseja converter {}?'.format(num))
conv = int(input('Digite 1 para binário, 2 para octal ou 3 para hexadecimal: '))
if conv == 1:
    print('{} em binário é igual a {}!'.format(num, bin(num)))
elif conv == 2:
    print('{} em octal é igual a {}!'.format(num, oct(num)))
elif conv == 3:
    print('{} em hexadecimal é igual {}!'.format(num, hex(num)))
else:
    print('Valor inválido! Digite um número de 1 a 3.')
