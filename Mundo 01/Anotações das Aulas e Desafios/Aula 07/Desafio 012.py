"""
DESAFIO 012: Calculando Descontos

Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
"""
p = float(input('Qual é o preço do produto? '))
d = p * 0.05
r = p - d
print('\nO produto que custa $ {:.2f} fica por $ {:.2f} com 5% de desconto ($ {:.2f}).'.format(p, r, d))
