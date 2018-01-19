"""
DESAFIO 035: Analisando Triângulo v1.0

Desenvolva um programa que leia o comprimento de três retas
e diga ao usuário se elas podem ou não formar um triângulo.
"""
r1 = float(input('Digite um número para o valor da primeira reta: '))
r2 = float(input('Digite um número para o valor da segunda reta: '))
r3 = float(input('Digite um número para o valor da terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As retas {} x {} x {} podem formar um triângulo!'.format(r1, r2, r3))
else:
    print('As retas {} x {} x {} não podem formar um triângulo!'.format(r1, r2, r3))
