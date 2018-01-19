"""
DESAFIO 013: Reajuste Salarial

Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
"""
s = float(input('Qual é o salário do funcionário? '))
a = s * 0.15
r = s + a
print('\nO salário atual é $ {:.2f}, e com o aumento de 15% ($ {:.2f}) ficará $ {:.2f}!'.format(s, a, r))
