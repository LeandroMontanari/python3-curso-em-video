"""
DESAFIO 078: Maior e Menor Valores na Lista

Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre
qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
"""
lista = list()
for n in range(0, 5):
    lista.append(int(input(f'Digite um valor para a Posição {n}: ')))
maximo = max(lista)
minimo = min(lista)
print('-=' * 25)
print(f'Você digitou os valores {lista}')

print(f'O maior valor digitado foi {maximo} nas posições ', end='')
for i, v in enumerate(lista):
    if v == maximo:
        print(f'{i}... ', end='')

print(f'\nO menor valor digitado foi {minimo} nas posições ', end='')
for i, v in enumerate(lista):
    if v == minimo:
        print(f'{i}... ', end='')

print('')
