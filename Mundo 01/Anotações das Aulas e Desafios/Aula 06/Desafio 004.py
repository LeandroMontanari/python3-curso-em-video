"""
DESAFIO 004: Dissecando uma Variável

Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
e todas as informações possíveis sobre ele.
"""
n = input('Digite algo: ')
print(n.isalnum())
print(n.isalpha())
print(n.isdecimal())
print(n.isdigit())
print(n.isidentifier())
print(n.islower())
print(n.isnumeric())
print(n.isprintable())
print(n.isspace())
print(n.istitle())
print(n.isupper())
