"""
DESAFIO 033: Maior e Menor Valores

Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
"""
n1 = int(input('Digite o primeiro número inteiro (ex: 10): '))
n2 = int(input('Digite o segundo número inteiro (ex: 15): '))
n3 = int(input('Digite o terceiro número inteiro (ex: 20): '))
menor = n1
maior = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O menor número é o {} e o maior é o {}!'.format(menor, maior))
