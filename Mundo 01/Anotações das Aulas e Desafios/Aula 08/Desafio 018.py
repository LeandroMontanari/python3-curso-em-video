"""
DESAFIO 018: Seno, Cosseno e Tangente

Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
"""
from math import radians, sin, cos, tan
a = float(input('Digite o ângulo para calcular: '))
ac = radians(a)
s = sin(ac)
c = cos(ac)
t = tan(ac)
print('\nO seno de {:.2f}º é {:.2f}, o cosseno é {:.2f}, e a tangente é {:.2f}!'.format(a, s, c, t))
